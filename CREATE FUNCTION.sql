CREATE OR REPLACE FUNCTION addInstruction(IN FrequencyInput VARCHAR, IN Amount DECIMAL(12,2), IN Customer VARCHAR, IN Administrator VARCHAR, IN Code VARCHAR, IN Notes VARCHAR, OUT result CHAR)AS $$

DECLARE FCode VARCHAR;

BEGIN

SELECT FrequencyCode INTO FCode FROM frequency WHERE frequencydesc = FrequencyInput;

INSERT INTO InvestInstruction (Amount, Frequency, ExpiryDate, Customer, Administrator, Code, Notes) 
VALUES (Amount, FCode, CURRENT_DATE + INTERVAL '1 Y', LOWER(Customer), Administrator, UPPER(Code), Notes);

END; $$ LANGUAGE plpgsql;

------------------------

CREATE OR REPLACE FUNCTION updateInstruction(IN AmountIn DECIMAL(12,2), IN FrequencyIn VARCHAR, IN ExpiryDateIn DATE, IN CustomerIn VARCHAR, IN AdministratorIn VARCHAR, IN CodeIn VARCHAR, IN NotesIn VARCHAR, IN Id INTEGER, OUT result CHAR)
AS $$

BEGIN

UPDATE investinstruction 
SET amount = AmountIn, frequency = FrequencyIn, expiryDate = ExpiryDateIn, customer = LOWER(CustomerIn), administrator = AdministratorIn, code = UPPER(CodeIn), notes = NotesIn
WHERE instructionId = Id;

END; $$ LANGUAGE plpgsql;