from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
from celery.utils.log import get_task_logger  
from celery.decorators import task 

from merchant.models import Celerytime 

import datetime
 
logger = get_task_logger(__name__)  
 
@periodic_task(  
    run_every=(crontab(minute='*/1')),  
    name="task_save_latest_flickr_image",  
    ignore_result=True  
)  
def task_save_latest_flickr_image():  
	new_record = Celerytime(name='celery')
	new_record.save()
