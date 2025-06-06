from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DyeTrialsAssets: 


	# Image Rule Assets
	# 从庭院进入灵染试炼活动 
	I_FP_ACCESS = RuleImage(roi_front=(1192,317,36,34), roi_back=(1000,101,261,472), threshold=0.8, method="Template matching", file="./tasks/DyeTrials/fp/fp_fp_access.png")
	# 寻找切换按钮 
	I_TOGGLE_BUTTON = RuleImage(roi_front=(1202,466,22,21), roi_back=(1090,127,176,377), threshold=0.7, method="Template matching", file="./tasks/DyeTrials/fp/fp_toggle_button.png")
	# 进入灵染试炼战斗界面 
	I_FP_ACCESS_1 = RuleImage(roi_front=(264,339,26,95), roi_back=(129,202,329,380), threshold=0.7, method="Template matching", file="./tasks/DyeTrials/fp/fp_fp_access_1.png")
	# 挑战 
	I_FP_CHALLENGE = RuleImage(roi_front=(1159,598,60,29), roi_back=(1159,598,60,29), threshold=0.8, method="Template matching", file="./tasks/DyeTrials/fp/fp_fp_challenge.png")
	# description 
	I_BATTLE_SUCCESS = RuleImage(roi_front=(435,147,100,100), roi_back=(435,147,100,100), threshold=0.8, method="Template matching", file="./tasks/DyeTrials/fp/battle_success.png")


	# Ocr Rule Assets
	# 战斗次数 
	O_BATTLE_NUM = RuleOcr(roi=(1144,408,100,21), area=(1144,408,100,21), mode="DigitCounter", method="Default", keyword="", name="battle_num")


