import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0123456789',
  message: 'This is the code to verify your account',
};

const jobType = 'push_notification_code';

const job = queue.create(jobType, jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Job creation failed:', err);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
