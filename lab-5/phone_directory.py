"""
Title: Phone Directory

Task: John keeps a backup of his old personal phone book as a text file. On each line of the file he can find
    the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name
    between < and > and the address.
    Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with
    non-alpha-numeric characters (except inside phone number and name).
    Examples of John's phone book lines:
        "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
        " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
        "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
    Could you help John with a program that, given the lines of his phone book and a phone number num returns
    a string for this number : "Phone => num, Name => name, Address => adress"
    Input:
        "+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
        "133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n",
        "1-541-754-3010"
    Output:
        Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.

Note: It can happen that there are many people for a phone number num, then return : "Error => Too many people: num"
    or it can happen that the number num is not in the phone book, in that case return: "Error => Not found: num"
"""


def get_clear_row(row: str) -> str:
    replacements = ('!', '/', ';', ',', '_')
    for replacement in replacements:
        row = row.replace(replacement, " ")

    return row


def clear_phone_book(txt: str):
    for row in txt.splitlines():
        clear_row = get_clear_row(row)
        name = ''
        phone = ''
        address = ''

        for word in clear_row.split():
            if word.startswith('+'):
                phone = word
            elif word.startswith('<') or word.endswith('>'):
                name = name + word + ' '
            else:
                address = address + ' ' + word

        yield f"Phone => {phone}, Name => {name.strip()[1:-1]}, Address => {address.strip()}"


if __name__ == '__main__':
    text = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n" \
          "133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n" \
          "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
    print(list(clear_phone_book(text)))
