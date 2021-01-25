import json
from django.http import HttpResponse
import jwt
import time
import datetime
import logging

from utils import creat_token, get_info_from_token, return_error

logging.basicConfig(level=logging.INFO)


def login(request):
    try:
        res = json.loads(request.body)
        if res['username'] == 'admin' and res['password'] == '123456':
            info = {
                'role': 'admin',
                'username': res['username'],
                'userId': 1,
                'time': str(datetime.datetime.now() + datetime.timedelta(hours=2))
            }
            token = creat_token(info).decode()
            data = {
                'code': 20000,
                "data": {"token": token}
            }
            return HttpResponse(json.dumps(data))
        elif res['username'] == 'user' and res['password'] == '123456':
            info = {
                'role': 'user',
                'username': res['username'],
                'userId': '2',
                'time': str(datetime.datetime.now() + datetime.timedelta(hours=2))
            }
            token = creat_token(info).decode()
            data = {
                'code': 20000,
                "data": {"token": token}
            }
            return HttpResponse(json.dumps(data))
    except:
        datas = {
            'code': 40000,
            "data": {'msg': "账号或密码错误"},
        }
        return HttpResponse(json.dumps(datas))


def logout(request):
    data = {"code": 20000, "data": "success"}
    return HttpResponse(json.dumps(data))


def get_table_list(request):
    data = {"code": 20000, "data": {"total": 30, "items": [{"id": "990000199505100577",
                                                            "title": "Djtv plrbiodug xpjbddm hnqa bihtqpxr vdvcb nwnkgwsrr hnifr xhduxsu vycqnslfby bwifqtovu xfjwmmxf lgphqlxz yqay fdm sawommmgf ydcwx.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "2016-03-11 16:56:02", "pageviews": 1867},
                                                           {"id": "370000200711061134",
                                                            "title": "Jzucdoj brvs nkqypdskf ekrvhuuo sly ctnv jywjbxkjgs tfdcbp dpmqyruw ojodex hdulr fufsfrsuw nqtvyy.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2012-01-08 04:32:50", "pageviews": 1652},
                                                           {"id": "500000201810034325",
                                                            "title": "Lflrrhiqo rup dxnihst qiconoo ifljriu cdjrx sjfdwohl olx nmywtdm bcpqj kxuvyskphc zbdkrb oixlhnv wfv iep ziv.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1985-07-10 10:26:18", "pageviews": 4294},
                                                           {"id": "370000198810147670",
                                                            "title": "Wgepoabeb lepbnykr yttjgpoqt mseghn qffwonp cnuh lumlbu bpmomkq ejidf vgcrdpcmtt khwnwm hgbd qireyc keu ihkl lvr gdlgtavl doyccq eqwysb.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "1973-03-20 10:12:56", "pageviews": 2432},
                                                           {"id": "420000198505051773",
                                                            "title": "Xacxcghp bjcloqm tmbc dleim gsiypho tnpmjmlsob ugfpxuwjft hvc zem qexpfntsu jsmiahnod.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1980-06-26 18:46:19", "pageviews": 4971},
                                                           {"id": "500000198307158465",
                                                            "title": "Tktw hpwwuqduz kuvz hocyt kggnhn tbyb bjlmlj pfmk txznwf lntilge iseknz.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1989-04-25 21:32:13", "pageviews": 4838},
                                                           {"id": "430000201805263483",
                                                            "title": "Bcnj xvytiqex iovvx oorkmrbk xhm bjjukt ivczj fzqc ubo ipicvhgs sebgdyvba qzhwo qddr pdrflouxk vujwvtulbw crebtl ohli rudegf vvmiexbsg.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2011-01-31 23:36:51", "pageviews": 4112},
                                                           {"id": "150000201403055510",
                                                            "title": "Pcpyuv nmjiuw bwjyqlhk fhbyqx ecinrzjvw yhobh zroxukwus jymgf mgvrxdf ghrcetx bptfnmbo iznwntl.",
                                                            "status": "published", "author": "name",
                                                            "display_time": "2000-07-25 20:08:58", "pageviews": 3653},
                                                           {"id": "450000198611133786",
                                                            "title": "Gkfculs fxothiuod yefqx unetpyl uks cpbfqacit ffxxotnoim qcyfl lvsejkcj ldoxdjadd lyjt eyg opiqen scwzpwm voiqlintyd bfjcclr cavpsd.",
                                                            "status": "published", "author": "name",
                                                            "display_time": "2018-12-17 13:03:23", "pageviews": 1298},
                                                           {"id": "540000200001023135",
                                                            "title": "Izyrdtlla ftnapbxzeg rlnb tuf zdoelh rwstyq wtoo lqndhc vvggt mjichok kwjhbdu eal kfzitn jlp.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2007-12-21 03:31:08", "pageviews": 4218},
                                                           {"id": "650000198411139443",
                                                            "title": "Xhqwxhepqd fvtlzs hey xvcruvjwrv evllk otsyox jpzkirg dnzr vvuondhmf lkrliqdtx tcqvxxfki pvffknj.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2016-08-11 11:27:53", "pageviews": 3237},
                                                           {"id": "430000201306065503",
                                                            "title": "Bgxlv npydi lbj eyaxbdws uywov jgmi lemxytx jclvnury jkac xbslqizyeb uhuny qatgdgcid.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1979-05-07 03:11:54", "pageviews": 2795},
                                                           {"id": "410000201704267748",
                                                            "title": "Vnclrxj muudrma ateqyne fcbwfgw txfmhtby veuqpowt epeacnpbnt qymrr ufsqbbowa njwutfyq pvkh boyxljj.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1984-02-12 00:20:00", "pageviews": 4990},
                                                           {"id": "110000200510239065",
                                                            "title": "Svyexzt qorfte npibl yaqpwomrez fpjsryeg yuju nhphlxfw ctxbk jeibj sbnd upsxxpi ikjwmtmmf ohnnjmary vmrcb.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "1987-04-01 08:55:09", "pageviews": 4406},
                                                           {"id": "140000200901174022",
                                                            "title": "Upfxhqdn xihiwhq jzevwmh nuvftggf gwvtg hdwvenejn nrfyqh oxgyychlx qsgg uqrb ifjsdpobzg flebdqn zicofl qqdnjabklt jhwo glqtls fhfae bmmlslnk qwqhmrjbnn.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1970-07-31 23:40:41", "pageviews": 2805},
                                                           {"id": "520000197002227166",
                                                            "title": "Kurpr nifgw jkbqstqoc gohtemalp uxysl eokeox gfoy fywsgi jjevqtub brfwbhco lghcqy kwbyci hobyh uxm owcoyrrukk glxsqpuuo hhid sqrwvlv.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2016-08-21 01:51:21", "pageviews": 4719},
                                                           {"id": "350000198305186595",
                                                            "title": "Zseipauwu hunws eum jhcfiobr pxstyp hmmwye kkmkeque mtxfynv oiiubxbf flhoher vbrk dsqxqfpnl bpvuimogpk.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "2008-03-25 13:02:28", "pageviews": 2193},
                                                           {"id": "500000199703158488",
                                                            "title": "Pzu nuhopxo nlo rvbzrden hrksux mjmxpt kje kolnfminj ydnzdpi ogbrgvlfkr lhbgs golrkr rpmq.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "2007-04-06 12:59:23", "pageviews": 4603},
                                                           {"id": "510000199110143426",
                                                            "title": "Pikeece znx kpqrlvygb rfjgxb eprsbf jfubctr wgzgcrf pcnjraqmk mlfc ikebyzmn qpotgbyo llwxpkpshn blduo ioobu.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2007-01-19 09:43:29", "pageviews": 2776},
                                                           {"id": "320000199512030103",
                                                            "title": "Dgh yrvpyy jbhom yfcyp oyljlt mfvxq nolup opdvlvuet fkbwel ihl qjwsng.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "2011-04-23 14:18:51", "pageviews": 4498},
                                                           {"id": "340000197903065332",
                                                            "title": "Spvalirjk cogtlfwmc ntwdmyb sdw oixwbgvpyv ycjedr jpfohyhru hbpmnehbej eiroib lejri kyxvby.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2014-04-21 13:31:20", "pageviews": 4655},
                                                           {"id": "440000197010037047",
                                                            "title": "Lsr gho aikf idyziaco lfeayt iqgjg hjhgdj ixjea wgnfhj xfsg zulq iotalf ktinuzueg jktkghu dnljsp vrwsgehxwm.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "1991-06-07 14:33:21", "pageviews": 1873},
                                                           {"id": "820000200803225043",
                                                            "title": "Wpfwm wneivihd ruvaj hkemd nrjye rfvjzlysm neovslhe biqvlgq lhk hhfhu xwjwituus ghe lxpu uxgzqiv pvqten flelv rxoqnja.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1978-08-07 07:23:53", "pageviews": 2516},
                                                           {"id": "140000198508117240",
                                                            "title": "Ltmwtjxcy nkxxitqw fahp ofqhxruhqa tnzgcxm lnrb xeqsr hqthl ljsqqxbwvy cjt rfuxnw iyof hrinb eyyngibf mvbvsxby.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1979-06-03 18:42:35", "pageviews": 854},
                                                           {"id": "450000198608238077",
                                                            "title": "Fswmblh gwdg slftzjvwu nsg nglgkqemg aybbqhnt fjzvlpdz zakkpev jvath zfp.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "1976-06-09 16:13:16", "pageviews": 2899},
                                                           {"id": "340000201707174514",
                                                            "title": "Uungvwwsy vhmdgoq boco xegef dbhalh toiufeps kheo eblqwy atuzrbgcn ogrchcy yruju iebdtdhcy crp.",
                                                            "status": "published", "author": "name",
                                                            "display_time": "1998-11-13 10:40:19", "pageviews": 4595},
                                                           {"id": "130000197507189609",
                                                            "title": "Bitlfho nfaghpvj yjbvroox kruby zybezwhr wruxikir zhe cednbroa owagpftqb fehczxqz ldlw rqlx wmpqjbztep edpifmih dxyb dyfmiqqzff.",
                                                            "status": "published", "author": "name",
                                                            "display_time": "2018-03-16 22:11:37", "pageviews": 910},
                                                           {"id": "510000199605082776",
                                                            "title": "Rtrvujfu pvmlu ccacwcfooh irmqst cfe vpdbp lldwwriaqb nsqb floe kblixuoi kvkd lmownsrq jyfivrd izg egvgarmy qcxhjey fxhywddssc qiw uscp.",
                                                            "status": "draft", "author": "name",
                                                            "display_time": "2004-12-08 18:26:52", "pageviews": 2540},
                                                           {"id": "520000198706117269",
                                                            "title": "Jwqoepvf dnm llnp cfegthktq gwpok ctksnfso vhtc ghhzhnvl xhllsg kvpb ufpvka knzjbsy lefeur mseu pamyesqj uxropqu hdlznxmipq jxlfxewdr jksom.",
                                                            "status": "published", "author": "name",
                                                            "display_time": "1986-07-09 04:06:24", "pageviews": 3429},
                                                           {"id": "32000019740103417X",
                                                            "title": "Yvcpw tknni ebnadra fmiclys ttgvrlj dgwyq utuxe spbvp vdjimshqvx hgspg uqzutegty dknistignc jwlloet.",
                                                            "status": "deleted", "author": "name",
                                                            "display_time": "1972-09-19 05:13:20", "pageviews": 1241}]}}
    return HttpResponse(json.dumps(data))


def get_info(request):
    token = request.headers.get('X-Token')
    try:
        info = get_info_from_token(token)
        if not info:
            raise Exception("token error")
        if info['role'] == 'admin':

            data = {"code": 20000, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                            "avatar": "https://cdn.jsdelivr.net/gh/icespite/picture@master/img/2019/logo.png",
                                            "name": "Super Admin"}}
            return HttpResponse(json.dumps(data))
        elif info['role'] == 'user':

            data = {"code": 20000, "data": {"roles": ["user"], "introduction": "I am a super administrator",
                                            "avatar": "https://cdn.jsdelivr.net/gh/icespite/picture@master/img/2019/avatar.png",
                                            "name": "just user"}}
            return HttpResponse(json.dumps(data))
    except Exception as e:
        logging.error(e)
        return HttpResponse(return_error())
