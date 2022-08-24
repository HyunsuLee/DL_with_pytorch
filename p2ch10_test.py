from p2ch10.vis import showCandidate
from p2ch10.vis import findPositiveSamples, showCandidate
from p2ch10.dsets import Ct, LunaDataset
positiveSample_list = findPositiveSamples()


series_uid = positiveSample_list[11][2]
ct = Ct(series_uid)
#print(ct.hu_a.squeeze(0).shape)

#print(series_uid)
showCandidate(series_uid) 

