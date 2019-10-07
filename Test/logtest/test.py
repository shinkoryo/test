# logging�Ǝ����datetime_module���C���|�[�g
import logging
import datetime_module
 
LOG_LEVEL_FILE = 'DEBUG'
LOG_LEVEL_CONSOLE = 'INFO'
 
# �t�H�[�}�b�g���w�� (https://docs.python.jp/3/library/logging.html#logrecord-attributes)
_detail_formatting = '%(asctime)s %(levelname)-8s [%(module)s#%(funcName)s %(lineno)d] %(message)s'
 
 
"""
LOG_LEVEL_FILE���x���ȏ�̃��O���t�@�C���ɏo�͂���ݒ�
"""
# datetime_module���W���[�����Ăяo����(test.py)�ŏo�͌`���Ȃǂ̊�{�ݒ������
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL_FILE), # LOG_LEVEL_FILE = 'DEBUG' �Ȃ� logging.DEBUG���w�肵�Ă��邱�ƂɂȂ�
    format=_detail_formatting,
    filename='.\logs\sample.log'
)
 
 
"""
LOG_LEVEL_CONSOLE���x���ȏ�̃��O���R���\�[��(std.stderr)�ɏo�͂���ݒ�
"""
# ���O���R���\�[���ɑ���n���h��console���쐬
console = logging.StreamHandler()
console.setLevel(getattr(logging, LOG_LEVEL_CONSOLE)) # LOG_LEVEL_CONSOLE = 'INFO' �Ȃ� logging.INFO���w�肵�Ă��邱�ƂɂȂ�
console_formatter = logging.Formatter(_detail_formatting)
console.setFormatter(console_formatter)
 
 
"""
console�n���h�������K�[�ɒǉ�����
"""
# test�p�̃��K�[���擾���Aconsole�n���h����ǉ�����
logger = logging.getLogger(__name__)
logger.addHandler(console)
# datetime_module�p�̃��K�[���擾���Aconsole�n���h����ǉ�����B���ɒǉ����������W���[��������Γ����`���Œǉ�����
logging.getLogger("datetime_module").addHandler(console)
 
 
if __name__ == '__main__':
 
    datetime_now = datetime_module.get_datetime_now()
 
    # ���O���o�͂�����@(���ۂɂ̓��O���o�͂������ꏊ�ŋL�q����)
    logger.debug('DEBUG���x���̃��b�Z�[�W�ł�')
    logger.info('INFO���x���̃��b�Z�[�W�ł�')
    logger.warning('WARNING���x���̃��b�Z�[�W�ł�')
    logger.error('ERROR���x���̃��b�Z�[�W�ł�')
    logger.critical('CRITICAL���x���̃��b�Z�[�W�ł�')
 
    monday_of_current_week = datetime_module.get_monday(datetime_now)