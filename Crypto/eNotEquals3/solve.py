import gmpy2

n = 442358020269025239784529881657908345803875059484134054141165593230517827485204479544632826166925881227509966668574539528280070688928011956508001796486806958524889587968125119593093967552951015478645997816271445440139381617683695840973328857781801825092231808293725745408481542703537506792627344769584006795958105733028652397390197811132273511794798642002630689036681091768602177392402221962104525972532003175995160603355152278093450084345115383953879655371054189302488195583963375326594691021240711707107726496770042093931660253751128787364174595528611392621132785316528529770174463347701858941962813233704556476643097591240913602980579773449976849741591074999626904101914254934812448154616526969756632929547982563461602310062192699132881293310554368825679738957006996270603144016820162384398763415065083535097209717004093694614002155390392165867801145931297061650087241278383758623310099000739530570568218761113354069071565343807867797402056044337052733405208796646722859876972431145379056960219711469220724728994737581072884921875507428857556634745637795620703114364700942184360550327009246516283113472432905237780991680997867003875945606737908288803088574148826637208419472536094098553501828160347965332904579074749956002695012777
e = 4
ct = 90184290829268731207627693777215198868804562964582318360753558136722085355933683743704932083861934846133432548371885994887690745251608757619527379630522977807420200869873736454183071251348638911254005746989490883770182361164873500534945361

m, result = gmpy2.iroot(ct,e)

try:
    flag = binascii.unhexlify(format(m, 'x')).decode()
except Exception as e:
    flag = m

hexed = hex(flag)[2:]
string = bytearray.fromhex(hexed).decode()
print(string)