CREATE MIGRATION m16fcy2cpqrsxjqumhogxxmh7gp5ebi6idzthpju4rhvo5obaskvfa
    ONTO m1jjrzi6styjz2c3om2itiopacyd6c55h7klyquv53pxyt33eajvzq
{
  ALTER TYPE default::Movie {
      CREATE INDEX ON (.title);
  };
};
