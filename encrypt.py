from substitution import substitution_result
from caesar_shift import caesar_shift_result
from cipher_stats import stats
from myutils import pline

pline()
caesar_shift_result('my name is john',1)
pline()
substitution_result('my name is john')
pline()
substitution_result('my friend and i would like to join you guys for dinner. we will be coming around when the sun sets.')
pline()
substitution_result("so many times, people told me I can't do this or can't do that. my nature is that I don't listen very well. "
	"I'm very determined, and I believe in myself. my parents brought me up that way. "+
	"thank god for that. I don't let anything stand in my way.")
pline()
stats('.chbnapgrlharlhphvdxtlhtpzghwdhudprhcdxhjxcihbdnhlprrgnehvghvptthfghod.prjhandxrlhv grhw ghixrhigwie')
pline()

