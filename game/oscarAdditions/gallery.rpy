init python:
    galleryCharacter = ""
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

label galleryNameChange:
    default persistent.mc_name = ""
    default persistent.sis_name = ""
    default persistent.sf_name = ""
    while persistent.mc_name == "" or persistent.sis_name == "" or persistent.sf_name == "":
        $ persistent.mc_name = renpy.input("What is your name?", default="Jack")
        $ persistent.sis_name = renpy.input("What is her name?", default="Eve")
        $ persistent.sf_name = renpy.input("What is the name of her friend?", default="Cassie")

    python:
        sisLovePath = "{}[{} Love Path]".format(gr, persistent.sis_name)
        sisLoveSubPath = "{}[{} SubLove Path]".format(gr, persistent.sis_name)
        sisSubPath = "{}[{} Sub Path]".format(gr, persistent.sis_name)
        sfLovePath = "{}[{} Love Path]".format(gr, persistent.sf_name)
        sfDomPath = "{}[{} Dom Path]".format(gr, persistent.sf_name)
        kellyPath = "{}[Kelly Path]".format(gr)
        assholePath = "{}[Asshole Path]".format(gr)

        sceneGalleryMenuDict = {
        "galleryMenu": [
        [persistent.sis_name, im.Crop("/images/ep1/ep1px0002.jpg", (0, 0, 1920, 1080))],
        [persistent.sf_name, "/images/ep1/ep1px0061.jpg"],
        ],
        persistent.sis_name: {
        1: [
        ["galleryScene1", {}, "/images/ep1/ep1px0049.jpg"],
        ["galleryScene2", {}, "/images/ep1/ep1px0056.jpg"],
        ["ep2sc2", {}, "/images/ep2/ep2_sc2_srm_15.jpg"],
        ["ep2sc10subroad", {}, "/images/ep2/ep2_sc10_ln_15.jpg"],
        ["ep2sc10creeproad", {"ep2cameraset":True}, "/images/ep2/ep2_sc10_ln_21.jpg"],
        ["galleryScene4", {"sis_submission":99}, "/images/ep3/ep3_sc3_shop_46.jpg"],
        ["galleryScene6", {"sis_submission":99}, "/images/ep3/ep3_sc16_kitchen_37.jpg"],
        ["galleryScene9", {"ep4dickjoke":True}, "/images/ep4/ep4_sc16_sr_39.jpg"],
        ],
        2: [
        ["ep4sc16", {"sis_sub_love_path":True, "sis_affection":99}, "/images/ep4/ep4_sc17_lr_42.jpg"],
        ["ep4sc16", {"sis_sub_love_path":True, "sis_affection":99}, "/images/ep4/ep4_sc17_lr_47.jpg"],
        ],
        },
        persistent.sf_name: {
        1: [
        ["galleryScene2", {}, "/images/ep1/ep1px0056.jpg"],
        ["galleryScene3", {}, "/images/ep2/ep2_sc1_m_k_7.jpg"],
        ["galleryScene5", {"ep3sfsislovechat":True, "sf_affection":99}, "/images/ep3/ep3_sc13_living_04.jpg"],
        ["ep3sc13", {"ep3handshaked":True}, "/images/ep3/ep3_sc13_living_34.jpg"],
        ["ep3sc13", {"ep3handshaked":False, "ep3facebroken":True}, "/images/ep3/ep3_sc13_living_37_bis.jpg"],
        ["galleryScene7", {}, "/images/ep4/ep4_sc13_mbr_04.jpg"],
        ["galleryScene8", {"sf_dominance":99}, "/images/ep4/ep4_sc15_mbr_37.jpg"],
        ],
        },
        }
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"
    text "Oscar's Scene Gallery":
        style "galleryHeader"
        xcenter 0.5
        ycenter 163

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "galleryBody"
                    xcenter 0.5

screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 0.5
        ycenter 163

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"mc_name":persistent.mc_name, "sis_name":persistent.sis_name, "sf_name":persistent.sf_name, "sisLovePath":sisLovePath, "sisLoveSubPath":sisLoveSubPath, "sisSubPath":sisSubPath, "sfLovePath":sfLovePath, "sfDomPath":sfDomPath}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
