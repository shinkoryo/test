# �K�v�ȃ��C�u�����ɉ�����logging���C���|�[�g
import datetime
import logging
 
# ���K�[���擾����
logger = logging.getLogger(__name__)
 
def get_datetime_now():
    """�v���O�������s���_�ł̓������v�Z����B
 
    Returns:
        datetime_now (datetime.datetime): �v���O�������s���_�ł̓���
    """
 
    # ���O���o�͂�����@(���ۂɂ̓��O���o�͂������ꏊ�ŋL�q����)
    logger.debug('DEBUG���x���̃��b�Z�[�W�ł�')
    logger.info('INFO���x���̃��b�Z�[�W�ł�')
    logger.warning('WARNING���x���̃��b�Z�[�W�ł�')
    logger.error('ERROR���x���̃��b�Z�[�W�ł�')
    logger.critical('CRITICAL���x���̃��b�Z�[�W�ł�')
 
    datetime_now = datetime.datetime.now()
 
    return datetime_now
 
def get_monday(time):
    """�w�肷��������܂܂��T�̌��j�����v�Z����B
 
    Args:
        time (datetime.datetime): �w�肷�����
 
    Returns:
        result (datetime.date): �w�肷��������܂܂��T�̌��j��
    """
 
    # ���O���o�͂�����@(���ۂɂ̓��O���o�͂������ꏊ�ŋL�q����)
    logger.debug('DEBUG���x���̃��b�Z�[�W�ł�')
    logger.info('INFO���x���̃��b�Z�[�W�ł�')
    logger.warning('WARNING���x���̃��b�Z�[�W�ł�')
    logger.error('ERROR���x���̃��b�Z�[�W�ł�')
    logger.critical('CRITICAL���x���̃��b�Z�[�W�ł�')
 
    time_date = time.date()
    weekday = time_date.weekday()
    delta = datetime.timedelta(days=weekday)
    result = time_date - delta
 
    return result