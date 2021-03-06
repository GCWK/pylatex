"""
    {
        "createdOn": "13 Mar 2018, Tue",
        "aim": "To create a simple letterhead document",
        "codedBy": "Rishikesh Agrawani"
    }
"""

import os

from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    TextColor, LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape
import lorem_ipsum
from pylatex.section import Paragraph

logo_name = "dell_logo.png"

def generate_unique():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options, document_options="a4paper")

    # Generating first page style
    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                         pos='c')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__),
                                     logo_name)
            logo_wrapper.append(StandAloneGraphic(image_options="width=50px",
                                filename=logo_file))

    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                 pos='c', align='r')) as title_wrapper:
            title_wrapper.append(LargeText(bold("Sjain ventures ltd")))
            title_wrapper.append(LineBreak())
            title_wrapper.append(MediumText(bold("C-246, Vallabhnagar")))
            title_wrapper.append(LineBreak())
            # title_wrapper.append(TextColor("gray", MediumText(bold("Raipur, CG"))))
            title_wrapper.append(MediumText(bold("Raipur, CG")))

    # Add footer
    # with first_page.create(Foot("C")) as footer:
    #     message = "Important message please read"
    #     with footer.create(Tabularx(
    #             "X X X X",
    #             width_argument=NoEscape(r"\textwidth"))) as footer_table:

    #         footer_table.add_row(
    #             [MultiColumn(4, align='l', data=TextColor("blue", message))])
    #         footer_table.add_hline(color="blue")
    #         footer_table.add_empty_row()

    #         branch_address = MiniPage(
    #             width=NoEscape(r"0.25\textwidth"),
    #             pos='t')
    #         branch_address.append("960 - 22nd street east")
    #         branch_address.append("\n")
    #         branch_address.append("Saskatoon, SK")

    #         document_details = MiniPage(width=NoEscape(r"0.25\textwidth"),
    #                                     pos='t', align='r')
    #         document_details.append("1000")
    #         document_details.append(LineBreak())
    #         document_details.append(simple_page_number())

    #         footer_table.add_row([branch_address, branch_address,
    #                               branch_address, document_details])

    # Newly added
    with first_page.create(Foot("L")) as right_footer:
        with right_footer.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                 pos='l', align='l')) as contact_wrapper:
            contact_wrapper.append(MediumText(bold("Alok Kumar Sharma")))
            contact_wrapper.append(LineBreak())
            contact_wrapper.append(MediumText("contact@sjainventures.com"))
            contact_wrapper.append(LineBreak())
            contact_wrapper.append(MediumText("+91 7877681234"))

    doc.preamble.append(first_page)
    # End first page style

    # Add customer information
    with doc.create(Tabu("X[r]")) as first_page_table:
        # customer = MiniPage(width=NoEscape(r"0.9\textwidth"), pos='h')
        # customer.append("Verna Volcano")
        # customer.append("\n")
        # customer.append("For some Person")
        # customer.append("\n")
        # customer.append("Address1")
        # customer.append("\n")
        # customer.append("Address2")
        # customer.append("\n")
        # customer.append("Address3")

        # Add branch information
        branch = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!',
                          align='r')
        branch.append("http://sjainventures.com")
        branch.append(LineBreak())
        branch.append("contact@sjainventures.com")
        # branch.append(LineBreak())
        # branch.append("+91 7877681234")

        first_page_table.add_row([branch]) # [customer, branch]
        first_page_table.add_empty_row()

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")

    # Add statement table
    # with doc.create(LongTabu("X[l] X[2l] X[r] X[r] X[r]",
    #                          row_height=1.5)) as data_table:
    #     data_table.add_row(["date",
    #                         "description",
    #                         "debits($)",
    #                         "credits($)",
    #                         "balance($)"],
    #                        mapper=bold,
    #                        color="lightgray")
    #     data_table.add_empty_row()
    #     data_table.add_hline()
    #     row = ["2016-JUN-01", "Test", "$100", "$1000", "-$900"]
    #     for i in range(25):
    #         if (i % 2) == 0:
    #             data_table.add_row(row, color="lightgray")
    #         else:
    #             data_table.add_row(row)

    with doc.create(Paragraph("Dear Rishikesh,")) as para1:
        para1.append(lorem_ipsum.LOREM_IPSUM_TEXT2)


    # doc.append(NewPage())

    # Add cheque images
    # with doc.create(LongTabu("X[c] X[c]")) as cheque_table:
    #     cheque_file = os.path.join(os.path.dirname(__file__),
    #                                'facebook_logo.png')
    #     cheque = StandAloneGraphic(cheque_file, image_options="width=200px")
    #     for i in range(0, 20):
    #         cheque_table.add_row([cheque, cheque])

    doc.generate_pdf("complex_report", clean_tex=False)

generate_unique()