import pysftp as sftp

"""Получение логов"""
# TODO Реализовать для получения json файлов и любых других

cnopts = sftp.CnOpts()
cnopts.hostkeys = None

with sftp.Connection('192.168.1.33', username='pad', password='1', cnopts=cnopts) as sftp:
    with sftp.cd('/home/pad/jetty/logs/'):             # temporarily chdir to public

        remotepath = r'/home/pad/jetty/logs/'

        localpath = 'C://work/ttv_autotest/qa_tools/tmp_files/'

        sftp.get_d(remotepath, localpath)




