# NOTE: \a is the delimiter for chat pages
# Quest ids can be found in Quests.py
SCRIPT = '''
ID reward_100
SHOW laffMeter
LERP_POS laffMeter 0 0 0 1
LERP_SCALE laffMeter 0.2 0.2 0.2 1
WAIT 1.5
ADD_LAFFMETER 1
WAIT 1
LERP_POS laffMeter -1.18 0 -0.87 1
LERP_SCALE laffMeter 0.075 0.075 0.075 1
WAIT 1
FINISH_QUEST_MOVIE

# TUTORIAL

ID tutorial_mickey
LOAD_SFX soundRun "phase_3.5/audio/sfx/AV_footstep_runloop.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_1 "phase_3/audio/dial/CC_%s_tutorial02.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_2 "phase_3.5/audio/dial/CC_tom_tutorial_%s01.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_3a "phase_3/audio/dial/CC_%s_tutorial03.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_3b "phase_3/audio/dial/CC_%s_tutorial05.ogg"
LOAD_DIALOGUE mickeyTutorialDialogue_4 "phase_3.5/audio/dial/CC_tom_tutorial_mickey02.ogg"
LOCK_LOCALTOON
REPARENTTO camera render
POSHPRSCALE camera 11 7 3 52 0 0 1 1 1
LOAD_CLASSIC_CHAR classicChar
REPARENTTO classicChar render
POS classicChar 0 0 0 
HPR classicChar 0 0 0
POS localToon 0 0 0
HPR localToon 0 0 0
WAIT 2
PLAY_SFX soundRun 1
LOOP_ANIM classicChar "run"
LOOP_ANIM localToon "run"
LERP_POS localToon -1.8 14.4 0 2
LERP_POS classicChar 0 17 0 2
WAIT 2
#LERP_HPR localToon -110 0 0 0.5
LERP_HPR localToon -70 0 0 0.5
LERP_HPR classicChar -120 0 0 0.5
WAIT 0.5
STOP_SFX soundRun
LOOP_ANIM localToon "neutral"
PLAY_ANIM classicChar "left-point-start" 1
WAIT 1.63
LOOP_ANIM classicChar "left-point"
CC_CHAT_CONFIRM classicChar "QuestScriptTutorial%s_1" mickeyTutorialDialogue_1
PLAY_ANIM classicChar "left-point-start" -1.5
WAIT 1.0867
LOOP_ANIM classicChar "neutral"
CC_CHAT_TO_CONFIRM npc classicChar "QuestScriptTutorial%s_2" "CFSpeech" mickeyTutorialDialogue_2
PLAY_ANIM classicChar "right-point-start" 1
WAIT 1.0867
LOOP_ANIM classicChar "right-point"
CC_CHAT_CONFIRM classicChar "QuestScriptTutorial%s_3" mickeyTutorialDialogue_3a mickeyTutorialDialogue_3b
PLAY_SFX soundRun 1
LOOP_ANIM classicChar "run"
LERP_HPR classicChar -180 0 0 0.5
WAIT 0.5
LERP_POS classicChar 0 0 0 2
WAIT 2
STOP_SFX soundRun
REPARENTTO classicChar hidden
UNLOAD_CHAR classicChar
#CHAT npc QuestScriptTutorialMickey_4 mickeyTutorialDialogue_4
REPARENTTO camera localToon
POS localToon 1.6 9.8 0
HPR localToon 14 0 0
FREE_LOCALTOON
LOCAL_CHAT_PERSIST npc QuestScriptTutorialMickey_4 mickeyTutorialDialogue_4

ID quest_assign_101
CLEAR_CHAT npc
LOAD squirt1 "phase_3.5/models/gui/tutorial_gui" "squirt1"
LOAD squirt2 "phase_3.5/models/gui/tutorial_gui" "squirt2"
LOAD toonBuilding "phase_3.5/models/gui/tutorial_gui" "toon_buildings"
LOAD cogBuilding "phase_3.5/models/gui/tutorial_gui" "suit_buildings"
LOAD cogs "phase_3.5/models/gui/tutorial_gui" "suits"
LOAD tart "phase_3.5/models/props/tart"
LOAD flower "phase_3.5/models/props/squirting-flower"
LOAD_DIALOGUE tomDialogue_01 "phase_3.5/audio/dial/CC_tom_tutorial_questscript01.ogg"
LOAD_DIALOGUE tomDialogue_02 "phase_3.5/audio/dial/CC_tom_tutorial_questscript03.ogg"
LOAD_DIALOGUE tomDialogue_03 "phase_3.5/audio/dial/CC_tom_tutorial_questscript04.ogg"
LOAD_DIALOGUE tomDialogue_04 "phase_3.5/audio/dial/CC_tom_tutorial_questscript05.ogg"
LOAD_DIALOGUE tomDialogue_05 "phase_3.5/audio/dial/CC_tom_tutorial_questscript06.ogg"
LOAD_DIALOGUE tomDialogue_06 "phase_3.5/audio/dial/CC_tom_tutorial_questscript07.ogg"
LOAD_DIALOGUE tomDialogue_07 "phase_3.5/audio/dial/CC_tom_tutorial_questscript08.ogg"
LOAD_DIALOGUE tomDialogue_08 "phase_3.5/audio/dial/CC_tom_tutorial_questscript09.ogg"
LOAD_DIALOGUE tomDialogue_09 "phase_3.5/audio/dial/CC_tom_tutorial_questscript10.ogg"
LOAD_DIALOGUE tomDialogue_10 "phase_3.5/audio/dial/CC_tom_tutorial_questscript11.ogg"
LOAD_DIALOGUE tomDialogue_11 "phase_3.5/audio/dial/CC_tom_tutorial_questscript12.ogg"
LOAD_DIALOGUE tomDialogue_12 "phase_3.5/audio/dial/CC_tom_tutorial_questscript13.ogg"
LOAD_DIALOGUE tomDialogue_13 "phase_3.5/audio/dial/CC_tom_tutorial_questscript14.ogg"
LOAD_DIALOGUE tomDialogue_14 "phase_3.5/audio/dial/CC_tom_tutorial_questscript16.ogg"
POSHPRSCALE cogs -1.05 7 0 0 0 0 1 1 1
POSHPRSCALE toonBuilding -1.05 7 0 0 0 0 1 1 1
POSHPRSCALE cogBuilding -1.05 7 0 0 0 0 1 1 1
POSHPRSCALE squirt1 -1.05 7 0 0 0 0 1 1 1
POSHPRSCALE squirt2 -1.05 7 0 0 0 0 1 1 1
REPARENTTO camera npc
POS camera -2.2 5.2 3.3
HPR camera 215 5 0
WRTREPARENTTO camera localToon
PLAY_ANIM npc "right-hand-start" 1
WAIT 1
REPARENTTO cogs aspect2d
LERP_SCALE cogs 1 1 1 0.5
WAIT 1.0833
LOOP_ANIM npc "right-hand" 1
FUNCTION npc "angryEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_1 "CFSpeech" tomDialogue_01
LOCAL_CHAT_CONFIRM npc QuestScript101_2 "CFSpeech" tomDialogue_02
REPARENTTO cogs hidden
REPARENTTO toonBuilding camera
LOCAL_CHAT_CONFIRM npc QuestScript101_3 "CFSpeech" tomDialogue_03
REPARENTTO toonBuilding hidden
REPARENTTO cogBuilding camera
FUNCTION npc "sadEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_4 "CFSpeech" tomDialogue_04
REPARENTTO cogBuilding hidden
REPARENTTO squirt1 camera
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_5 "CFSpeech" tomDialogue_05
REPARENTTO squirt1 hidden
REPARENTTO squirt2 camera
LOCAL_CHAT_CONFIRM npc QuestScript101_6 "CFSpeech" tomDialogue_06
PLAY_ANIM npc 'right-hand-start' -1.8
LERP_SCALE squirt2 1 1 0.01 0.5
WAIT 0.5
REPARENTTO squirt2 hidden
WAIT 0.6574
LOOP_ANIM npc 'neutral' 1
LOCAL_CHAT_CONFIRM npc QuestScript101_7 "CFSpeech" tomDialogue_07
# Make it look like the client has no inventory. Since the toon.dc
# specifies that the user really does have 1 of each item, we will 
# just put on a show for the client of not having any items then
# handing them out.
SET_INVENTORY 4 0 0
SET_INVENTORY 5 0 0
REPARENTTO inventory camera
SHOW inventory
SET_INVENTORY_DETAIL -1
POSHPRSCALE inventory -0.77 7.42 1.11 0 0 0 0.01 0.01 0.01
SET_INVENTORY_YPOS 4 0  -0.1
SET_INVENTORY_YPOS 5 0  -0.1
LERP_SCALE inventory 3 0.01 3 1
WAIT 1
REPARENTTO flower npc "**/1000/**/def_joint_right_hold"
POSHPRSCALE flower 0.10 -0.14 0.20 180.00 287.10 168.69 0.70 0.70 0.70
PLAY_ANIM npc 'right-hand-start' 1.8
WAIT 1.1574
LOOP_ANIM npc 'right-hand' 1.1
WAIT 0.8
WRTREPARENTTO flower camera
LERP_POSHPRSCALE flower -1.75 4.77 0.00 30.00 180.00 16.39 0.75 0.75 0.75 0.589
WAIT 1.094
LERP_POSHPRSCALE flower -1.76 7.42 -0.63 179.96 -89.9 -153.43 0.12 0.12 0.12 1
PLAY_ANIM npc 'right-hand-start' -1.5
WAIT 1
ADD_INVENTORY 5 0 1
POSHPRSCALE inventory -0.77 7.42 1.11 0 0 0 3 0.01 3
REPARENTTO flower hidden
REPARENTTO tart npc "**/1000/**/def_joint_right_hold"
POSHPRSCALE tart 0.19 0.02 0.00 0.00 0.00 349.38 0.34 0.34 0.34
PLAY_ANIM npc 'right-hand-start' 1.8
WAIT 1.1574
LOOP_ANIM npc 'right-hand' 1.1
WAIT 0.8
WRTREPARENTTO tart camera
LERP_POSHPRSCALE tart -1.37 4.56 0 329.53 39.81 346.76 0.6 0.6 0.6 0.589
WAIT 1.094
LERP_POSHPRSCALE tart -1.66 7.42 -0.36 0 30 30 0.12 0.12 0.12 1.0
PLAY_ANIM npc 'right-hand-start' -1.5
WAIT 1
ADD_INVENTORY 4 0 1
POSHPRSCALE inventory -0.77 7.42 1.11 0 0 0 3 0.01 3
REPARENTTO tart hidden
#PLAY_ANIM npc 'neutral' 1
#WAIT 2.0833
PLAY_ANIM npc 'right-hand-start' 1
WAIT 1.0
HIDE inventory
REPARENTTO inventory hidden
SET_INVENTORY_YPOS 4 0  0
SET_INVENTORY_YPOS 5 0  0
SET_INVENTORY_DETAIL 0
POSHPRSCALE inventory 0 0 0 0 0 0 1 1 1
OBSCURE_LAFFMETER 0
SHOW laffMeter
POS laffMeter 0 0 0
SCALE laffMeter 0.075 0.075 0.075
LERP_POS laffMeter 1.7 0 0.87 1
LERP_SCALE laffMeter 0.2 0.2 0.2 0.6
WAIT 1.0833
LOOP_ANIM npc "right-hand"
LOCAL_CHAT_CONFIRM npc QuestScript101_8 "CFSpeech" tomDialogue_08
LOCAL_CHAT_CONFIRM npc QuestScript101_9 "CFSpeech" tomDialogue_09
FUNCTION npc "sadEyes"
FUNCTION npc "blinkEyes"
LAFFMETER 15 15
WAIT 0.1
LAFFMETER 14 15
WAIT 0.1
LAFFMETER 13 15
WAIT 0.1
LAFFMETER 12 15
WAIT 0.1
LAFFMETER 11 15
WAIT 0.1
LAFFMETER 10 15
WAIT 0.1
LAFFMETER 9 15
WAIT 0.1
LAFFMETER 8 15
WAIT 0.1
LAFFMETER 7 15
WAIT 0.1
LAFFMETER 6 15
WAIT 0.1
LAFFMETER 5 15
WAIT 0.1
LAFFMETER 4 15
WAIT 0.1
LAFFMETER 3 15
WAIT 0.1
LAFFMETER 2 15
WAIT 0.1
LAFFMETER 1 15
WAIT 0.1
LAFFMETER 0 15
LOCAL_CHAT_CONFIRM npc QuestScript101_10 "CFSpeech" tomDialogue_10
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
LAFFMETER 15 15
WAIT 0.5
LERP_POS laffMeter 0.15 0.15 0.15 1
LERP_SCALE laffMeter 0.085 0.085 0.085 0.6
PLAY_ANIM npc "right-hand-start" -2
WAIT 1.0625
LOOP_ANIM npc "neutral"
WAIT 0.5
LERP_HPR npc -50 0 0 0.5
FUNCTION npc "surpriseEyes"
FUNCTION npc "showSurpriseMuzzle"
PLAY_ANIM npc "right-point-start" 1.5
WAIT 0.6944
LOOP_ANIM npc "right-point"
LOCAL_CHAT_CONFIRM npc QuestScript101_11 "CFSpeech" tomDialogue_11
LOCAL_CHAT_CONFIRM npc QuestScript101_12 "CFSpeech" tomDialogue_12
PLAY_ANIM npc "right-point-start" -1
LERP_HPR npc -0.068 0 0 0.75
WAIT 1.0417
FUNCTION npc "angryEyes"
FUNCTION npc "blinkEyes"
FUNCTION npc "hideSurpriseMuzzle"
LOOP_ANIM npc "neutral"
FUNCTION localToon "questPage.showQuestsOnscreenTutorial"
LOCAL_CHAT_CONFIRM npc QuestScript101_13 "CFSpeech" tomDialogue_13
FUNCTION localToon "questPage.hideQuestsOnscreenTutorial"
LOCAL_CHAT_CONFIRM npc QuestScript101_14 1 "CFSpeech" tomDialogue_14
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
# Cleanup
UPON_TIMEOUT FUNCTION tart "removeNode"
UPON_TIMEOUT FUNCTION flower "removeNode"
UPON_TIMEOUT FUNCTION cogs "removeNode"
UPON_TIMEOUT FUNCTION toonBuilding "removeNode"
UPON_TIMEOUT FUNCTION cogBuilding "removeNode"
UPON_TIMEOUT FUNCTION squirt1 "removeNode"
UPON_TIMEOUT FUNCTION squirt2 "removeNode"
UPON_TIMEOUT LOOP_ANIM npc "neutral"
UPON_TIMEOUT HIDE inventory
UPON_TIMEOUT SET_INVENTORY_DETAIL 0
UPON_TIMEOUT SHOW laffMeter
UPON_TIMEOUT POS laffMeter 0.15 0.15 0.15
UPON_TIMEOUT SCALE laffMeter 0.085 0.085 0.085
UPON_TIMEOUT POSHPRSCALE inventory 0 0 0 0 0 0 1 1 1
POS localToon 0.776 14.6 0
HPR localToon 47.5 0 0
FINISH_QUEST_MOVIE

# TUTORIAL HQ HARRY

ID quest_incomplete_110
DEBUG "quest assign 110"
LOAD_DIALOGUE harryDialogue_01 "phase_3.5/audio/dial/CC_harry_tutorial_questscript01.ogg"
LOAD_DIALOGUE harryDialogue_02 "phase_3.5/audio/dial/CC_harry_tutorial_questscript02.ogg"
LOAD_DIALOGUE harryDialogue_03 "phase_3.5/audio/dial/CC_harry_tutorial_questscript03.ogg"
LOAD_DIALOGUE harryDialogue_04 "phase_3.5/audio/dial/CC_harry_tutorial_questscript04.ogg"
LOAD_DIALOGUE harryDialogue_05 "phase_3.5/audio/dial/CC_harry_tutorial_questscript05.ogg"
LOAD_DIALOGUE harryDialogue_06 "phase_3.5/audio/dial/CC_harry_tutorial_questscript06.ogg"
LOAD_DIALOGUE harryDialogue_07 "phase_3.5/audio/dial/CC_harry_tutorial_questscript07.ogg"
LOAD_DIALOGUE harryDialogue_08 "phase_3.5/audio/dial/CC_harry_tutorial_questscript08.ogg"
LOAD_DIALOGUE harryDialogue_09 "phase_3.5/audio/dial/CC_harry_tutorial_questscript09.ogg"
LOAD_DIALOGUE harryDialogue_10 "phase_3.5/audio/dial/CC_harry_tutorial_questscript10.ogg"
LOAD_DIALOGUE harryDialogue_11 "phase_3.5/audio/dial/CC_harry_tutorial_questscript11.ogg"
SET_MUSIC_VOLUME 0.4 activityMusic 0.5 0.7
LOCAL_CHAT_CONFIRM npc QuestScript110_1 harryDialogue_01
OBSCURE_BOOK 0
SHOW bookOpenButton
LOCAL_CHAT_CONFIRM npc QuestScript110_2 harryDialogue_02
# ARROWS_ON 0.92 -0.89 0 1.22 -0.64 90
ARROWS_ON 1.364477 -0.89 0 1.664477 -0.64 90
LOCAL_CHAT_PERSIST npc QuestScript110_3 harryDialogue_03
WAIT_EVENT "enterStickerBook"
ARROWS_OFF
SHOW_BOOK
HIDE bookPrevArrow
HIDE bookNextArrow
CLEAR_CHAT npc
WAIT 0.5
TOON_HEAD npc -0.2 -0.45 1
LOCAL_CHAT_CONFIRM npc QuestScript110_4 harryDialogue_04
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_5 harryDialogue_05
WAIT_EVENT "stickerBookPageChange-3"
HIDE bookPrevArrow
HIDE bookNextArrow
ARROWS_OFF
CLEAR_CHAT npc
WAIT 0.5
LOCAL_CHAT_CONFIRM npc QuestScript110_6 harryDialogue_06
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_7 harryDialogue_07
WAIT_EVENT "stickerBookPageChange-4"
HIDE bookNextArrow
HIDE bookPrevArrow
ARROWS_OFF
CLEAR_CHAT npc
LOCAL_CHAT_CONFIRM npc QuestScript110_8 harryDialogue_08
LOCAL_CHAT_CONFIRM npc QuestScript110_9 harryDialogue_09
LOCAL_CHAT_PERSIST npc QuestScript110_10 harryDialogue_10
ENABLE_CLOSE_BOOK
ARROWS_ON 1.364477 -0.89 0 1.664477 -0.64 90
WAIT_EVENT "exitStickerBook"
ARROWS_OFF
TOON_HEAD npc 0 0 0
HIDE_BOOK
HIDE bookOpenButton
LOCAL_CHAT_CONFIRM npc QuestScript110_11 1 harryDialogue_11
SET_MUSIC_VOLUME 0.7 activityMusic 1.0 0.4
# Lots of cleanup
UPON_TIMEOUT DEBUG "testing upon death"
UPON_TIMEOUT OBSCURE_BOOK 0
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT HIDE_BOOK
UPON_TIMEOUT COLOR_SCALE bookOpenButton 1 1 1 1
UPON_TIMEOUT TOON_HEAD npc 0 0 0
UPON_TIMEOUT SHOW bookOpenButton
FINISH_QUEST_MOVIE

# TUTORIAL FLIPPY

ID tutorial_blocker
LOAD_DIALOGUE blockerDialogue_01 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker01.ogg"
LOAD_DIALOGUE blockerDialogue_02 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker02.ogg"
LOAD_DIALOGUE blockerDialogue_03 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker03.ogg"
LOAD_DIALOGUE blockerDialogue_04 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker04.ogg"
LOAD_DIALOGUE blockerDialogue_05a "phase_3.5/audio/dial/CC_flippy_tutorial_blocker05.ogg"
LOAD_DIALOGUE blockerDialogue_05b "phase_3.5/audio/dial/CC_flippy_tutorial_blocker06.ogg"
LOAD_DIALOGUE blockerDialogue_06 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker07.ogg"
LOAD_DIALOGUE blockerDialogue_07 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker08.ogg"
LOAD_DIALOGUE blockerDialogue_08 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker09.ogg"
HIDE localToon
REPARENTTO camera npc
FUNCTION npc "stopLookAround"
#POS camera 0.0 6.0 4.0
#HPR camera 180.0 0.0 0.0
LERP_POSHPR camera 0.0 6.0 4.0 180.0 0.0 0.0 0.5
SET_MUSIC_VOLUME 0.4 music 0.5 0.8
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_1 blockerDialogue_01
WAIT 0.8 
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_2 blockerDialogue_02
WAIT 0.8 
#POS camera -5.0 -9.0 6.0
#HPR camera -25.0 -10.0 0.0
LERP_POSHPR camera -5.0 -9.0 6.0 -25.0 -10.0 0.0 0.5
POS localToon 203.8 18.64 -0.475
HPR localToon -90.0 0.0 0.0
SHOW localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_3 blockerDialogue_03
OBSCURE_CHAT 1 0
SHOW chatScButton
WAIT 0.6 
ARROWS_ON -1.3644 0.91 180 -1.5644 0.74 -90 
LOCAL_CHAT_PERSIST npc QuestScriptTutorialBlocker_4 blockerDialogue_04
WAIT_EVENT "enterSpeedChat"
ARROWS_OFF
BLACK_CAT_LISTEN 1
WAIT_EVENT "SCChatEvent"
BLACK_CAT_LISTEN 0
WAIT 0.5
CLEAR_CHAT localToon
REPARENTTO camera localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_5 "CFSpeech" blockerDialogue_05a blockerDialogue_05b
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_6 "CFSpeech" blockerDialogue_06
OBSCURE_CHAT 0 0 
SHOW chatNormalButton
WAIT 0.6 
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_7 "CFSpeech" blockerDialogue_07
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_8 1 "CFSpeech" blockerDialogue_08
SET_MUSIC_VOLUME 0.8 music 1.0 0.4
LOOP_ANIM npc "walk"
LERP_HPR npc 270 0 0 0.5
WAIT 0.5
LOOP_ANIM npc "run"
LERP_POS npc 217.4 18.81 -0.475 0.75 
LERP_HPR npc 240 0 0 0.75 
WAIT 0.75
LERP_POS npc 222.4 15.0 -0.475 0.35
LERP_HPR npc 180 0 0 0.35
WAIT 0.35
LERP_POS npc 222.4 5.0 -0.475 0.75
WAIT 0.75
REPARENTTO npc hidden
FREE_LOCALTOON
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT OBSCURE_CHAT 0 0 
UPON_TIMEOUT REPARENTTO camera localToon
FINISH_QUEST_MOVIE

# TUTORIAL TROLLEY

ID gag_intro
SEND_EVENT "disableGagPanel"
SEND_EVENT "disableBackToPlayground"
HIDE inventory
TOON_HEAD npc 0 0 1
WAIT 0.1
# Welcome to the Gag Shop!
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_1
LERP_POS npcToonHead -0.64 0 -0.74 0.7
LERP_SCALE npcToonHead 0.82 0.82 0.82 0.7
LERP_COLOR_SCALE purchaseBg 1 1 1 1  0.6 0.6 0.6 1 0.7
WAIT 0.7
SHOW inventory
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_1a
## here's your jb jar
#ARROWS_ON -1.22 0.09 0 -0.93 -0.2 -90 
#LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_2
#ARROWS_OFF
# try buying a gag
ARROWS_ON -0.19 0.04 180 -0.4 0.26 90
LOCAL_CHAT_PERSIST npc QuestScriptGagShop_3
SEND_EVENT "enableGagPanel"
WAIT_EVENT "inventory-selection"
ARROWS_OFF
CLEAR_CHAT npc
WAIT 0.5
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_4
# show advanced throw & squirt gags
LOCAL_CHAT_PERSIST npc QuestScriptGagShop_5
WAIT 0.5
SHOW_THROW_SQUIRT_PREVIEW
CLEAR_CHAT npc
WAIT 0.5
# show "Exit Back To Playground" button
SET_BIN backToPlaygroundButton "gui-popup"
LERP_POS backToPlaygroundButton -0.12 0 0.18 0.5
LERP_SCALE backToPlaygroundButton 2 2 2 0.5
LERP_COLOR_SCALE backToPlaygroundButton 1 1 1 1  2.78 2.78 2.78 1 0.5
LERP_COLOR_SCALE inventory 1 1 1 1  0.6 0.6 0.6 1 0.5
WAIT 0.5
START_THROB backToPlaygroundButton 2.78 2.78 2.78 1  2.78 2.78 2.78 0.7  2
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_6
STOP_THROB
LERP_POS backToPlaygroundButton 0.72 0 -0.045 0.5
LERP_SCALE backToPlaygroundButton 1.04 1.04 1.04 0.5
LERP_COLOR_SCALE backToPlaygroundButton 2.78 2.78 2.78 1  1 1 1 1 0.5
WAIT 0.5
CLEAR_BIN backToPlaygroundButton
# show "Play Again" button
SET_BIN playAgainButton "gui-popup"
LERP_POS playAgainButton -0.12 0 0.18 0.5
LERP_SCALE playAgainButton 2 2 2 0.5
LERP_COLOR_SCALE playAgainButton 1 1 1 1  2.78 2.78 2.78 1 0.5
WAIT 0.5
START_THROB playAgainButton 2.78 2.78 2.78 1  2.78 2.78 2.78 0.7  2
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_7
STOP_THROB
LERP_POS playAgainButton 0.72 0 -0.24 0.5
LERP_SCALE playAgainButton 1.04 1.04 1.04 0.5
LERP_COLOR_SCALE playAgainButton 2.78 2.78 2.78 1  1 1 1 1 0.5
WAIT 0.5
CLEAR_BIN playAgainButton
# You're needed in Toon HQ!
LOCAL_CHAT_CONFIRM npc QuestScriptGagShop_8 1
TOON_HEAD npc 0 0 0
LERP_COLOR_SCALE inventory 0.6 0.6 0.6 1  1 1 1 1 0.5
LERP_COLOR_SCALE purchaseBg 0.6 0.6 0.6 1  1 1 1 1 0.5
WAIT 0.5
SEND_EVENT "enableBackToPlayground"
UPON_TIMEOUT TOON_HEAD npc 0 0 0
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT SHOW inventory
UPON_TIMEOUT SEND_EVENT "enableGagPanel"
UPON_TIMEOUT SEND_EVENT "enableBackToPlayground"

ID quest_incomplete_120
CHAT_CONFIRM npc QuestScript120_1
# ANIM
CHAT_CONFIRM npc QuestScript120_2 1
FINISH_QUEST_MOVIE

ID quest_assign_121
CHAT_CONFIRM npc QuestScript121_1 1
FINISH_QUEST_MOVIE

ID quest_assign_130
CHAT_CONFIRM npc QuestScript130_1 1
FINISH_QUEST_MOVIE

ID quest_assign_131
CHAT_CONFIRM npc QuestScript131_1 1
FINISH_QUEST_MOVIE

ID quest_assign_140
CHAT_CONFIRM npc QuestScript140_1 1
FINISH_QUEST_MOVIE

ID quest_assign_141
CHAT_CONFIRM npc QuestScript141_1 1
FINISH_QUEST_MOVIE

# TUTORIAL COG

ID quest_incomplete_145
CHAT_CONFIRM npc QuestScript145_1 1
LOAD frame "phase_4/models/gui/tfa_images" "FrameBlankA"
LOAD tunnel "phase_4/models/gui/tfa_images" "tunnelSignA"
POSHPRSCALE tunnel 0 0 0 0 0 0 0.8 0.8 0.8
REPARENTTO tunnel frame
POSHPRSCALE frame 0 0 0 0 0 0 0.1 0.1 0.1
REPARENTTO frame aspect2d
LERP_SCALE frame 1.0 1.0 1.0 1.0
WAIT 3.0
LERP_SCALE frame 0.1 0.1 0.1 0.5
WAIT 0.5
REPARENTTO frame hidden
CHAT_CONFIRM npc QuestScript145_2 1
UPON_TIMEOUT FUNCTION frame "removeNode"
FINISH_QUEST_MOVIE

# TUTORIAL FRIENDS

ID quest_incomplete_150
CHAT_CONFIRM npc QuestScript150_1
ARROWS_ON  1.65 0.51 -120 1.65 0.51 -120
SHOW_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_2
ARROWS_OFF
HIDE_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_3
HIDE bFriendsList
CHAT_CONFIRM npc QuestScript150_4 1
UPON_TIMEOUT HIDE_FRIENDS_LIST
UPON_TIMEOUT ARROWS_OFF
FINISH_QUEST_MOVIE

# First Task: Assign Visit to Jester Chester
ID quest_assign_600
PLAY_ANIM npc "wave" 1
CHAT npc QuestScript600_1
LOAD_IMAGE logo "phase_3/maps/toontown-logo.png"
REPARENTTO logo aspect2d
POSHPRSCALE logo -0.4 7 0 0 0 0 0 0 0
LERP_SCALE logo 0.4 0.2 0.2 0.5
WAIT 2.5
LOOP_ANIM npc "neutral"
LERP_SCALE logo 0 0 0 0.5
WAIT 0.5
FUNCTION logo "destroy"
CLEAR_CHAT npc
CHAT_CONFIRM npc QuestScript600_2
CHAT_CONFIRM npc QuestScript600_3
CHAT_CONFIRM npc QuestScript600_4
CHAT_CONFIRM npc QuestScript600_5
PLAY_ANIM npc "wave" 1
CHAT_CONFIRM npc QuestScript600_6
LOOP_ANIM npc "neutral"
FINISH_QUEST_MOVIE
'''