import requests

from bs4 import BeautifulSoup

# a = "https://gogo.exchange/server/api/v1/send_message"
# requests.post(url='http://194.87.62.91:8005/api/v1/send_message', json={'res': 1})
# requests.post(url='https://kumicho.pw/api/v1/send_message', json={'res': 1})

html = """\n\t\t\t
<div class="xchangestep2bodyvn">
\t\t\t\n\t\t\n\t\t\t<div class="stepblock">
\n\t\t\t\t<div class="steptitle">Отдаете <span class="steptitlemin">С учетом комиссии платежной системы <b>Bitcoin</b></span>
</div>\n\t\t\t\t<div class="stepblleft">\n\t\t\t\t\n\t\t\t\t\t<p><span class="steptitsumm">Сумма:</span> 
<b>0.1389</b> <span class="steptitvtype">Bitcoin BTC</span></p>\n\t\t\t\t\t<p><span class="steptitsumm">Со счета:</span>
 <b>1231232</b></p>\n\t\t\t\t</div>\n\t\t\t\t<div class="stepblright">\n\t\t\t\t\t<div class="stepicotext">Bitcoin BTC</div>
 \n\t\t\t\t\t<div class="stepico" style="background: url(/wp-content/uploads/coins/bitcoin.svg) no-repeat center center;">
 </div>\n\t\t\t\t\t\t<div class="clear"></div>\n\t\t\t\t</div>\n\t\t\t\t\t<div class="clear"></div>\n\t\t\t</div>\n\t\t\t\n\t\t\t
 <div class="stepblock">\n\t\t\t\t<div class="steptitle">Получаете <span class="steptitlemin">
 С учетом комиссии платежной системы <b>Сбербанк</b></span></div>\n\t\t\t\t<div class="stepblleft">\n\t\t\t\t\t\n\t\t\t\t\t<p>
 <span class="steptitsumm">Сумма:</span> <b>200004.556</b> <span class="steptitvtype">Сбербанк RUB</span></p>\n\t\t\t\t\t<p>
 <span class="steptitsumm">На карту:</span> <b>2202 2036 5757 2090</b></p>\n\t\t\t\t</div>\n\t\t\t\t<div class="stepblright">\n\t\t\t\t\t
 <div class="stepicotext">Сбербанк RUB</div>\n\t\t\t\t\t<div class="stepico" style="background: url(/wp-content/uploads/coins/sberbank.svg) 
 no-repeat center center;"></div>\t\t\t\t\n\t\t\t\t\n\t\t\t\t\t<div class="clear"></div>\n\t\t\t\t</div>\t\t\t\t\n\t\t\t\t\t<div class="clear">
 </div>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class="stepblock lichdann">\n\t\t\t\t<div class="steptitle">Личные данные</div>\n\t\t\t\t\n\t\t\t\t
 <div class="lichdannvn">\n\t\t\t\t\n\t\t\t\t\t<div class="stepline"><span class="step2name">Имя:</span> Администратор</div>
 \n\t\t\t\t\t\n\t\t\t\t\t<div class="stepline"><span class="step2name">E-mail:</span> sadsad@mail.ru</div>\n\t\t\t\t\n\t\t\t\t\t
 <div class="stepline"><span class="step2name">Телефон:</span> 819938848281</div>\n\t\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\t
 <div class="stepcheckbox">\n\t\t        <div class="checkbox act" id="check_rule_step"><input type="checkbox" id="createzajatos" name="" value="1"> С <a href="https://gogo.exchange/tos/">правилами сервиса</a> ознакомлен и согласен</div>\n\t\t    </div>\n\t\t\t<div class="biginfo">\n\t\t\t    <div class="biginfovn">\n\t\t\t\t    <div class="binfotitle">Внимание!</div>\n\t\t\t\t    Использование сервиса после нажатия кнопки «Создать заявку» означает, что вы принимаете все основные требования, предъявляемые к Пользователю сервиса.\n\t\t\t    </div>\n\t\t\t</div>\n\t\t    <div class="stepwarning">Внимательно проверьте правильность платежных данных перед созданием заявки!</div>\n\t\t\t\n            <form action="https://gogo.exchange/ajax-createbids.html?meth=post&amp;yid=3f4d0ec5d934" class="ajax_post_form" method="post">\n\t\t\t\t<input type="hidden" name="hash" value="PrqHnbSsTsbEvXOJmgV22AYPufGlpEO4iGo">\n\t\t\t\t<div class="step2submit">\n\t\t            <input type="submit" name="" formtarget="_top" id="createzaja" value="Создать заявку">\n\t\t        </div>\n\n\t\t\t\t<div class="ajax_post_bids_res" style="padding: 10px 0px;">\n\t\t\t\t\t<div class="resultgo"></div>\n\t\t\t\t</div>\t\t\t\t\n            </form>\t\t\t\n\t\t\t\n\t\t\t</div>\n\t\t"""

soup = BeautifulSoup(html, 'lxml')

block = soup.select('div.stepblock')
block_lk = soup.select_one('div.stepblock.lichdann')

print(f"""
{block[0].select_one('div.steptitle').text}
{block[0].select_one('div.stepblleft').text}
{block[1].select_one('div.steptitle').text}
{block[1].select_one('div.stepblleft').text}
{block_lk.text}
""")