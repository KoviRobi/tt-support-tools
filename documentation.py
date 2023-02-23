import logging
import re
import subprocess
import os
import glob
import gdstk
import cairosvg


# doc check
# makes sure that the basic info is present
def check_yaml_docs(yaml):
    logging.info("checking docs")
    for key in ['author', 'title', 'description', 'how_it_works', 'how_to_test', 'language', 'inputs', 'outputs']:
        if key not in yaml['documentation']:
            logging.error("missing key {} in documentation".format(key))
            exit(1)
        if yaml['documentation'][key] == "":
            logging.error("missing value for {} in documentation".format(key))
            exit(1)

    # if provided, check discord handle is valid
    if len(yaml['documentation']['discord']):
        parts = yaml['documentation']['discord'].split('#')
        if len(parts) != 2 or len(parts[0]) == 0 or not re.match('^[0-9]{4}$', parts[1]):
            logging.error('Invalid format for discord username')
            exit(1)


# use pandoc to create a single page PDF preview
def create_pdf(yaml):
    yaml = yaml['documentation']
    logging.info("creating pdf")
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir, "docs/project_header.md")) as fh:
        doc_header = fh.read()
    with open(os.path.join(script_dir, "docs/project_preview.md")) as fh:
        doc_template = fh.read()

    with open('datasheet.md', 'w') as fh:
        fh.write(doc_header)
        # handle pictures
        yaml['picture_link'] = ''
        if yaml['picture']:
            # skip SVG for now, not supported by pandoc
            picture_name = yaml['picture']
            if 'svg' not in picture_name:
                yaml['picture_link'] = '![picture]({})'.format(picture_name)
            else:
                logging.warning("svg not supported")

        # now build the doc & print it
        try:
            doc = doc_template.format(**yaml)
            fh.write(doc)
            fh.write("\n\pagebreak\n")
        except IndexError:
            logging.warning("missing pins in info.yaml, skipping")

    pdf_cmd = 'pandoc --pdf-engine=xelatex -i datasheet.md -o datasheet.pdf'
    logging.info(pdf_cmd)
    p = subprocess.run(pdf_cmd, shell=True)
    if p.returncode != 0:
        logging.error("pdf command failed")


# SVG and PNG renders of the GDS
def create_svg(args):
    gds = glob.glob(os.path.join(args.run_dir, 'results/final/gds/*gds'))
    library = gdstk.read_gds(gds[0])
    top_cells = library.top_level()
    top_cells[0].write_svg('gds_render.svg')

    if args.create_png:
        cairosvg.svg2png(url='gds_render.svg', write_to='gds_render.png')
