const nodemailer = require('nodemailer');

async function mySendMail(destination, subject, messageToSend) {
  let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: !!!Replace with Email to login,
      pass: !!!Replace with Password to login
    }
  });

  let mailOptions = {
    from: !!!Replace with From Email,
    to: destination,
    subject: subject,
    text: messageToSend
  };

  transporter.sendMail(mailOptions, function(error, info) {
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });
}

module.exports = mySendMail;