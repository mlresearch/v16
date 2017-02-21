import os
filenames = ['settles_jmlr10', 'index.html', 'ActiveChallenge_jxie.html', 'logo.png', 'jmlrwcp.html', 'aistats01Nov2010', 'pjmlr2010b.html', 'tomanek', 'tomanek.html', 'introduction.html', 'gp_jmlr_wcp_rev.html', 'aistats01Nov2010.html', 'al_datamin.html', 'jmlrwcp', 'introduction', 'aistats-workshop-5.html', 'yukun.html', 'jmlr.css', 'pjmlr2010b', 'ActiveChallenge_jxie', 'gp_jmlr_wcp_rev', 'al_datamin', 'aistats-workshop-5', 'yukun', 'lovell_paper', 'settles_jmlr10.html', 'lovell_paper.html']
nameids = []
for n in filenames:
    if n.find('.html') > 0:
        fields = n.split('.')
        nameids.append(fields[0])

namdict = {'ActiveChallenge_jxie':'xie11a',
           'aistats-workshop-5':'lan11a',
           'aistats01Nov2010':'borisov11a',
           'al_datamin':'bodo11a',
           'gp_jmlr_wcp_rev':'geist11a',
           'introduction':'guyon11a',
           'jmlrwcp':'ho11a',
           'lovell_paper':'lovel11a',
           'pjmlr2010b':'cawley11a',
           'settles_jmlr10':'settles11a',
           'tomanek':'tomanek11a',
           'yukun':'chen11a']


