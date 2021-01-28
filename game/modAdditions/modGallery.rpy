init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = os.path.join("/images/", "{}".format(thumbnail))
            if not self in galleryItems: galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    def galleryMenu():
        rv = [
            [persistent.sis_name, im.Crop("/images/ep1/ep1px0002.jpg", (0, 0, 1920, 1080))],
            [persistent.sf_name, "/images/ep1/ep1px0061.jpg"],
            ["Other", "/images/ep1/ep1px0061.jpg"],
        ]
        return rv

default galleryPageNumber = 1
default scopeDict = {}

# python:
#     sisLovePath = "{}[{} Love Path]".format(gr, persistent.sis_name)
#     sisLoveSubPath = "{}[{} SubLove Path]".format(gr, persistent.sis_name)
#     sisSubPath = "{}[{} Sub Path]".format(gr, persistent.sis_name)
#     sfLovePath = "{}[{} Love Path]".format(gr, persistent.sf_name)
#     sfDomPath = "{}[{} Dom Path]".format(gr, persistent.sf_name)
#     kellyPath = "{}[Kelly Path]".format(gr)
#     assholePath = "{}[Asshole Path]".format(gr)


label galleryNameChange:
    default persistent.mc_name = ""
    default persistent.sis_name = ""
    default persistent.sf_name = ""
    if persistent.mc_name == "":
        $ persistent.mc_name = renpy.input("What is your name?", default="Jack")
    if persistent.sis_name == "":
        $ persistent.sis_name = renpy.input("What is her name?", default="Eve")
    if persistent.sf_name == "":
        $ persistent.sf_name = renpy.input("What is the name of her friend?", default="Cassie")

    $ scopeDict = { "mc_name":persistent.mc_name, "sis_name":persistent.sis_name, "sf_name":persistent.sf_name }

    $ Eve = GalleryItem(persistent.sis_name, 1, "galleryScene1", "ep1/ep1px0049.jpg")
    $ Eve = GalleryItem(persistent.sis_name, 1, "galleryScene2", "ep1/ep1px0056.jpg")
    $ Eve = GalleryItem(persistent.sis_name, 1, "ep2sc2", "ep2/ep2_sc2_srm_15.jpg")
    $ Eve = GalleryItem(persistent.sis_name, 1, "ep2sc10subroad", "ep2/ep2_sc10_ln_15.jpg")
    $ Eve = GalleryItem(persistent.sis_name, 1, "ep2sc10creeproad", "ep2/ep2_sc10_ln_21.jpg", {"ep2cameraset":True})
    $ Eve = GalleryItem(persistent.sis_name, 1, "galleryScene4", "ep3/ep3_sc3_shop_46.jpg", {"sis_submission":99})
    $ Eve = GalleryItem(persistent.sis_name, 1, "galleryScene6", "ep3/ep3_sc16_kitchen_37.jpg", {"sis_submission":99})
    $ Eve = GalleryItem(persistent.sis_name, 1, "galleryScene9", "ep4/ep4_sc16_sr_39.jpg", {"ep4dickjoke":True})
    $ Eve = GalleryItem(persistent.sis_name, 2, "ep4sc16", "ep4/ep4_sc17_lr_42.jpg", {"sis_sub_love_path":True, "sis_affection":99})
    $ Eve = GalleryItem(persistent.sis_name, 2, "galleryScene11", "ep5/ep5_sc23_lr_26.jpg", {"sis_sub_path":True, "sis_sub_love_path":True})
    $ Eve = GalleryItem(persistent.sis_name, 2, "galleryScene11", "ep5/ep5_sc23_lr_71.jpg", {"sis_sub_path":True})
    $ EveCassie = GalleryItem(persistent.sis_name, 2, "galleryScene12", "ep5/ep5_sc23_lr_95.jpg")
    $ Eve = GalleryItem(persistent.sis_name, 2, "galleryScene13", "ep5/ep5_sc24_lr_35.jpg")
    $ EveCassie = GalleryItem(persistent.sis_name, 2, "galleryScene14", "ep5/ep5_sc25_sr_44.jpg")

    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene2", "ep1/ep1px0056.jpg")
    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene3", "ep2/ep2_sc1_m_k_7.jpg")
    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene5", "ep3/ep3_sc13_living_04.jpg", {"ep3sfsislovechat":True, "sf_affection":99})
    $ Cassie = GalleryItem(persistent.sf_name, 1, "ep3sc13", "ep3/ep3_sc13_living_34.jpg", {"ep3handshaked":True})
    $ Cassie = GalleryItem(persistent.sf_name, 1, "ep3sc13", "ep3/ep3_sc13_living_37_bis.jpg", {"ep3handshaked":False, "ep3facebroken":True})
    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene7", "ep4/ep4_sc13_mbr_04.jpg")
    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene8", "ep4/ep4_sc15_mbr_37.jpg", {"sf_dominance":99})
    $ Cassie = GalleryItem(persistent.sf_name, 1, "galleryScene10", "ep5/ep5_sc10_mcr_42.jpg", {"ep4willingsodom":True})
    $ Cassie = GalleryItem(persistent.sf_name, 2, "ep5sc21", "ep5/ep5_sc21_mbr_26.jpg", {"ep5sftruelove":True})
    $ Cassie = GalleryItem(persistent.sf_name, 2, "ep5sc21", "ep5/ep5_sc21_mbr_59.jpg")
    $ Cassie = GalleryItem(persistent.sf_name, 2, "ep5sc22", "ep5/ep5_sc22_mbr_20.jpg", {"ep5totaldom":True, "ep5sorrydom":True})
    $ EveCassie = GalleryItem(persistent.sf_name, 2, "galleryScene12", "ep5/ep5_sc23_lr_95.jpg")
    $ EveCassie = GalleryItem(persistent.sf_name, 2, "galleryScene14", "ep5/ep5_sc25_sr_44.jpg")

    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu():
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action Function(galleryDecreasePageNumber)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)