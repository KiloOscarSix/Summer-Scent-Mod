define gr = "{color=#0f0}"
define red = "{color=#f00}"
define blue = "{color=#00f}"

define mod = Character("OscarSix", color="#0f0")
define config.menu_include_disabled = True

define Recommended = "{color=#00f}[Recommended]"
define EndRelationship = "{color=#f00}[End Relationship]"

label walkthroughVars:
    $ sisLovePath = "{}[{} Love Path]".format(gr, sis_name)
    $ sisLoveSubPath = "{}[{} SubLove Path]".format(gr, sis_name)
    $ sisSubPath = "{}[{} Sub Path]".format(gr, sis_name)
    $ sfLovePath = "{}[{} Love Path]".format(gr, sf_name)
    $ sfDomPath = "{}[{} Dom Path]".format(gr, sf_name)
    $ kellyPath = "{}[Kelly Path]".format(gr)
    $ hatePath = "{}[Hate Path]".format(gr)
    $ sfSisPath = "{}[{}+{} Path]".format(gr, sis_name, sf_name)
    
    $ modSisHelped = "[{} Helped]".format(sis_name)
    $ modSisAbused = "[{} Abused]".format(sis_name)

    return

label after_load:
    call walkthroughVars

    return