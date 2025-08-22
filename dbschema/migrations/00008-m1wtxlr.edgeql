CREATE MIGRATION m1wtxlrj4xxtt7ydzswyfdqdc2bpxk4omotqhdw3sbe5faxdk3moia
    ONTO m125gxd3qfaxp4tg45lverygm5ofxmcvxa2zak2wyiiperlyiwdb3a
{
  ALTER TYPE default::ParticipantDate {
      ALTER PROPERTY storred {
          RENAME TO starred;
      };
  };
};
