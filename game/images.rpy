transform left1:
    xpos 0.10 xanchor 0.0 ypos 1.0 yanchor 1.0

transform right1:
    xpos 0.9 xanchor 1.0 ypos 1.0 yanchor 1.0

transform lefthinata:
    xpos 0.05 xanchor 0.0 ypos 1.0 yanchor 1.0
    zoom 0.9

transform righthinata:
    xpos 1.0 xanchor 1.0 ypos 1.0 yanchor 1.0
    zoom 0.9

transform leftmom:
    xpos -0.1 xanchor 0.0 ypos 1.0 yanchor 0.9

transform lefthag:
    xpos 0.00 xanchor 0.0 ypos 1.0 yanchor 1.0

transform lefthp:
    xpos 0.00 xanchor 0.0 ypos 1.0 yanchor 1.0
    zoom 0.9

transform lefthb:
    xpos 0.0 xanchor 0.0 ypos 1.0 yanchor 1.0

transform rightw:
    xpos 0.9 xanchor 1.0 ypos 1.0 yanchor 1.1
    zoom 0.9

image hat =  ConditionSwitch(
            "_last_say_who == 'k'", "hat.png",
            "not _last_say_who == 'k'", "hatgrey.png")

image dhat =  ConditionSwitch(
            "_last_say_who == 'dk'", "dhat.png",
            "not _last_say_who == 'dk'", "dhatgrey.png")

image police =  ConditionSwitch(
            "_last_say_who == 'p'", "police.png",
            "not _last_say_who == 'p'", "policegrey.png")

image zan =  ConditionSwitch(
            "_last_say_who == 'z'", "zan.png",
            "not _last_say_who == 'z'", "zangrey.png")
image yui =  ConditionSwitch(
            "_last_say_who == 'y'", "yui.png",
            "not _last_say_who == 'y'", "yuigrey.png")
image nana =  ConditionSwitch(
            "_last_say_who == 'n'", "nana.png",
            "not _last_say_who == 'n'", "nanagrey.png")
image hinata =  ConditionSwitch(
            "_last_say_who == 'h'", "hinata.png",
            "not _last_say_who == 'h'", "hinatagrey.png")
image hag =  ConditionSwitch(
            "_last_say_who == 'h1'", "hag.png",
            "not _last_say_who == 'h1'", "haggrey.png")
image xenia =  ConditionSwitch(
            "_last_say_who == 'x'", "xenia.png",
            "not _last_say_who == 'x'", "xeniagrey.png")

image hatfence =  ConditionSwitch(
            "_last_say_who == 'k'", "hatfence.png",
            "not _last_say_who == 'k'", "hatfencegrey.png")
image hatbondwast =  ConditionSwitch(
            "_last_say_who == 'k'", "hatbondwast.png",
            "not _last_say_who == 'k'", "hatbondwastgrey.png")

image nanafence =  ConditionSwitch(
            "_last_say_who == 'n'", "nanafence.png",
            "not _last_say_who == 'n'", "nanafencegrey.png")
image cat =  ConditionSwitch(
            "_last_say_who == 'i'", "cat.png",
            "not _last_say_who == 'i'", "catgrey.png")
image mom =  ConditionSwitch(
            "_last_say_who == 'm'", "mommy.png",
            "not _last_say_who == 'm'", "mommygrey.png")
image nanab =  ConditionSwitch(
            "_last_say_who == 'n'", "nanab.png",
            "not _last_say_who == 'n'", "nanabgrey.png")
image nanap =  ConditionSwitch(
            "_last_say_who == 'n'", "nanap.png",
            "not _last_say_who == 'n'", "nanapgrey.png")
image yuip =  ConditionSwitch(
            "_last_say_who == 'y'", "yuip.png",
            "not _last_say_who == 'y'", "yuipgrey.png")
image xeniap =  ConditionSwitch(
            "_last_say_who == 'x'", "xeniap.png",
            "not _last_say_who == 'x'", "xeniapgrey.png")
image hinatap =  ConditionSwitch(
            "_last_say_who == 'h'", "hinatap.png",
            "not _last_say_who == 'h'", "hinatapgrey.png")
image hatp =  ConditionSwitch(
            "_last_say_who == 'k'", "hatp.png",
            "not _last_say_who == 'k'", "hatpgrey.png")
image wwyd =  ConditionSwitch(
            "_last_say_who == 'w'", "wwyd.png",
            "not _last_say_who == 'w'", "wwydg.png")



image mai=Image("mai.png")
image bart=Image("bart.png")
image osamu=Image("osamu.png")
