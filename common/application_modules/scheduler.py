import apscheduler.executors.asyncio
import apscheduler.jobstores.mongodb
import apscheduler.schedulers.asyncio

from common.application_modules.module import ApplicationModule

scheduler_job_store = {"default": apscheduler.jobstores.mongodb.MongoDBJobStore()}
scheduler_executors = {"default": apscheduler.executors.asyncio.AsyncIOExecutor()}

scheduler = apscheduler.schedulers.asyncio.AsyncIOScheduler(
    jobstores=scheduler_job_store, executors=scheduler_executors
)


class ScheduleModule(ApplicationModule):
    def __init__(self):
        self.scheduler = scheduler

    def start(self, config, loop):
        self.scheduler._eventloop = loop
        self.scheduler.start()
