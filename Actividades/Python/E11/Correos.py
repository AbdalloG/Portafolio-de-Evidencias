import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

De = "steam.powered.valve.r@outlook.com"
Para = "fec63c53.uanl.edu.mx@amer.teams.ms "
Contra = getpass.getpass("Contra: ")
subject = "Recibo de su pago a Steam "

newMessage = MIMEMultipart()                         
newMessage['From'] = De                  
newMessage['To'] = Para
newMessage['Subject'] = subject  


html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
    <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#eeeeee"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table cellpadding="0" cellspacing="0" class="es-content esd-header-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="7954" align="center">
                                        <table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p15t es-p15b es-p10r es-p10l" align="left">
                                                        <!--[if mso]><table width="580" cellpadding="0" cellspacing="0"><tr><td width="282" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="282" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-empty-container" style="display: none;"></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="278" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="278" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-empty-container" style="display: none;"></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr></tr>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="7681" align="center">
                                        <table class="es-header-body" style="background-color: #044767;" width="600" cellspacing="0" cellpadding="0" bgcolor="#044767" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p35t es-p35b es-p35r es-p35l" align="left" bgcolor="#221e21" style="background-color: #221e21;">
                                                        <table cellspacing="0" cellpadding="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left">
                                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td class="esd-block-text" align="right">
                                                                                                        <p><br></p>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                    <td class="esd-block-image es-p10l" valign="top" align="left" style="font-size: 0px;">
                                                                                        <a href="" target="_blank"><img src="https://demo.stripocdn.email/content/guids/665615e2-f04b-4cca-9f26-a679486659b8/images/steam_rbez.jpg" alt style="display: block;" width="120"></a>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-m-txt-c" align="left">
                                                                                        <h1><br></h1>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p35r es-p35l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p25t es-p25b es-p35r es-p35l" align="center" style="font-size:0">
                                                                                        <a target="_blank" href=""><img src="https://tlr.stripocdn.email/content/guids/CABINET_75694a6fc3c4633b3ee8e3c750851c02/images/67611522142640957.png" alt style="display: block;" width="120"></a>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10b" align="center">
                                                                                        <h2><strong>Gracias por tu transacción reciente en Steam.</strong></h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p15t es-p20b" align="left">
                                                                                        <p style="font-size: 16px; color: #777777;">Los artículos a continuación se han añadido a tu biblioteca de Steam.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p35r es-p35l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p10b es-p10r es-p10l" bgcolor="#eeeeee" align="left">
                                                                                        <table style="width: 500px;" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td width="80%">
                                                                                                        <h4>Order Confirmation #</h4>
                                                                                                    </td>
                                                                                                    <td width="20%">
                                                                                                        <h4>2345678</h4>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p35r es-p35l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t es-p10b es-p10r es-p10l" align="left">
                                                                                        <table style="width: 500px;" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                                        <p><strong>Worms Rumble</strong></p>
                                                                                                    </td>
                                                                                                    <td style="padding: 5px 0" width="20%" align="left">
                                                                                                        <p>Mex$ 14.65</p>
                                                                                                    </td>
                                                                                                </tr>
                                                                                                <tr>
                                                                                                    <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                                        <p>IVA (16&nbsp;%):</p>
                                                                                                    </td>
                                                                                                    <td style="padding: 5px 0" width="20%" align="left">
                                                                                                        <p>Mex$ 2.34</p>
                                                                                                    </td>
                                                                                                </tr>
                                                                                                <tr>
                                                                                                    <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                                        <p><br></p>
                                                                                                    </td>
                                                                                                    <td style="padding: 5px 0" width="20%" align="left">
                                                                                                        <p><br></p>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p10t es-p35r es-p35l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table style="border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;" width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p15t es-p15b es-p10r es-p10l" align="left">
                                                                                        <table style="width: 500px;" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td width="80%">
                                                                                                        <h4>TOTAL</h4>
                                                                                                    </td>
                                                                                                    <td width="20%">
                                                                                                        <h4><strong>Mex$ 16.99</strong></h4>
                                                                                                    </td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p40t es-p40b es-p35r es-p35l" esd-custom-block-id="7796" align="left">
                                                        <!--[if mso]><table width="530" cellpadding="0" cellspacing="0"><tr><td width="255" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame es-m-p20b" width="255" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p15b" align="left">
                                                                                        <h4>Valve Corporation</h4>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10b" align="left">
                                                                                        <p>PO Box 1688<br>Bellevue, WA 98009<br>United States<br>Id. de IVA: VCO030424EXA<br><br>Ten en cuenta que esto no es una dirección de devolución.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="255" valign="top"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="255" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p15b" align="left">
                                                                                        <h4>Estimated Delivery Date<br></h4>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text" align="left">
                                                                                        <p>27-04-2022</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="7797" align="center">
                                        <table class="es-content-body" style="background-color: #1b9ba3;" width="600" cellspacing="0" cellpadding="0" bgcolor="#1b9ba3" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p35t es-p35b es-p35r es-p35l" align="left" bgcolor="#221e21" style="background-color: #221e21;">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p25t" align="center">
                                                                                        <h2 style="color: #ffffff; font-size: 24px;">Get 25% off your next order.</h2>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p30t es-p15b es-p10r es-p10l" align="center"><span class="es-button-border" style="background: #1d40ca;"><a href="" class="es-button" target="_blank" style="background: #1d40ca; border-color: #1d40ca;">Awesome</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="7684" align="center">
                                        <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p35t es-p40b es-p35r es-p35l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="530" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p15b" align="center" style="font-size: 0px;">
                                                                                        <a target="_blank"><img src="https://demo.stripocdn.email/content/guids/665615e2-f04b-4cca-9f26-a679486659b8/images/steam_2016_logo_blacksvg.png" alt="Beretun logo" style="display: block;" title="Beretun logo" width="152"></a>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p35b" align="center">
                                                                                        <p><strong></strong>Para descargar el cliente de escritorio de Steam y aprender más sobre Steam, por favor, visita Acerca de Steam.<strong></strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td esdev-links-color="#777777" align="left" class="esd-block-text es-m-txt-c es-p5b">
                                                                                        <p style="color: #777777;"><strong>© Valve Corporation</strong><br><strong>PO Box 1688 Bellevue, WA 98009 (USA)</strong><br><br>Todos los derechos reservados. Todas las marcas registradas pertenecen a sus respectivos dueños en EE. UU. y otros países.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="esd-footer-popover es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-infoblock made_with" align="center" style="font-size: 0px;">
                                                                                        <a target="_blank" href=""><img src="https://demo.stripocdn.email/content/guids/665615e2-f04b-4cca-9f26-a679486659b8/images/1200pxvalvelogo.jpg" alt width="125" style="display: block;"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""
part1 = MIMEText(html, "html")
newMessage.attach(part1)


with open('D:\Perfil\Abdall\Escritorio\Recibo.png', 'rb') as f:
    data = f.read()
    part = MIMEImage(data, name="Recibo.png")
    newMessage.attach(part)
    f.close()
with open('D:\Perfil\Abdall\Escritorio\ReciboQR.png', 'rb') as f:
    data = f.read()
    part = MIMEImage(data, name="Recibo.png")
    newMessage.attach(part)
    f.close()


text = newMessage.as_string()

context = ssl.create_default_context()
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    smtp.starttls(context=context)
    smtp.login(De, Contra)              
    smtp.sendmail(De,Para,text)
    smtp.quit()
