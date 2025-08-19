CREATE MIGRATION m1jjrzi6styjz2c3om2itiopacyd6c55h7klyquv53pxyt33eajvzq
    ONTO m1hzq2sbc32slhoml2p37z7am2odvnwvr7stf2pahyk3bi76wlkeoq
{
  ALTER TYPE default::Movie {
      ALTER PROPERTY tilte {
          RENAME TO title;
      };
  };
};
