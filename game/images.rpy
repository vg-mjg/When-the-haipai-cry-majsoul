transform left1:
    xpos 0.10 xanchor 0.0 ypos 1.0 yanchor 1.0

transform right1:
    xpos 0.9 xanchor 1.0 ypos 1.0 yanchor 1.0




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

image mai=Image("mai.png")
image bart=Image("bart.png")
image osamu=Image("osamu.png")
