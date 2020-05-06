import os


power_template = "<div class=\"col-md-6 mb-3\">\
            <h4>Power Name<span class=\"badge badge-primary pull-right\">Type</span></h4>\
            <p>Describe Power</p>\
         </div>"
relationship_template = "<div class=\"col-md-6 mb-3\">\
            <h4><a href=LINK HERE>Name</a><span class=\"badge badge-primary pull-right\">Relationship</span></h4>\
            <p>Describe Relationship</p>\
         </div>"


def main():
    template = open_file("Template.html")
    tuple_array = tuple_array_builder(["NAME", "ELEMENT", "GENDER/PRONOUNS", "ORIENTATION", "CLASS", "AGE", "HABITAT", "BIRTHDAY", "IMAGE"])
    template = replace_words(tuple_array, template, "ENTRY.")
    powers = power_builder()
    print(powers)
    relations = relationship_builder()
    print(relations)
    autoentry_tuple_array = [("POWERS", powers), ("RELATIONSHIPS", relations)]
    template = replace_words(autoentry_tuple_array, template, "AUTOENTRY.")

    print(template)

    pass


def open_file(file_path):
    result = ""
    file = open(file_path)
    for line in file:
        result += line
    return result


def tuple_array_builder(fields):
    result = []
    for field in fields:
        replacement = input(field + ": ")
        result += [(field, replacement)]
    return result


def replace_words(tuple_array, template, keyword):
    result = template
    wordlen = len(keyword)
    for part in template.split(">"):
        for line in part.split("<"):
            if line[:wordlen] == keyword:
                for tup in tuple_array:
                    if line[wordlen:] == tup[0]:
                        result = result.replace(line, tup[1])
    return result


def power_builder():
    result = ""
    power_number = int(input("How many powers does this cat have? ").strip())
    for i in range(0, power_number):
        print("Power number: "+str(i+1))
        power_name = input("Power Name: ")
        power_type = input("Power Type: ")
        desc = input("Relationship Description: ")
        result += power_template.replace("Power Name", power_name)\
            .replace("Type", power_type)\
            .replace("Describe Power", desc)
    return result


def relationship_builder():
    result = ""
    rel_number = int(input("How many relations does this cat have? ").strip())
    for i in range(0, rel_number):
        print("Power number: " + str(i + 1))
        link = input("link: ")
        relationship = input("Relationship: ")
        desc = input("Power Description: ")
        result += power_template.replace("LINK HERE", link)\
            .replace("Relationship", relationship)\
            .replace("Describe Relationship", desc)
    return result

main()