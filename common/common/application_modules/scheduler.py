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
    def __init__(self, name):
        super().__init__(name)
        self.scheduler = scheduler

    def add_jobs(self):
        from game.models.world import CLOCK

        self.scheduler.add_job(
            CLOCK.tick,
            "interval",
            minutes=1,
        )

    def start(self, config, loop):
        self.scheduler.configure(event_loop=loop)
        self.scheduler.start()
        self.add_jobs()
