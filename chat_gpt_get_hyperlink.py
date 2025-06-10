from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import RGBColor

def add_hyperlink(paragraph, url, text_before_link, link_text, color="0000FF", underline=True):
    """
    Add a hyperlink to a paragraph.

    :param paragraph: The paragraph we are adding the hyperlink to.
    :param url: The URL for the hyperlink.
    :param text: The display text for the hyperlink.
    :param color: The font color in hex (default is blue).
    :param underline: Boolean to underline the text.
    """
    # Create the w:hyperlink tag and set its attributes
    part = paragraph.part
    r_id = part.relate_to(url, reltype="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    # Create a w:r element
    new_run = OxmlElement("w:r")

    # Create a w:rPr element
    rPr = OxmlElement("w:rPr")

    # Add color
    color_elem = OxmlElement("w:color")
    color_elem.set(qn("w:val"), color)
    rPr.append(color_elem)

    # Underline
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rPr.append(u)

    # Append w:rPr to w:r
    new_run.append(rPr)

    # Add the text
    t = OxmlElement("w:t")
    t.text = link_text
    new_run.append(t)

    # Add the run to the hyperlink
    hyperlink.append(new_run)

    paragraph.add_run(text_before_link)
    # Add the hyperlink to the paragraph
    paragraph._p.append(hyperlink)

    return paragraph