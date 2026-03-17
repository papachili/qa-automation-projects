*** Settings ***
Library    Browser

*** Variables ***
${FIELD_1}          id=lteq30a
${FIELD_2}          id=lteq30b
${VALUE_1}          id=_valuevalue1
${VALUE_2}          id=_valuevalue2
${ERROR_1}          id=lteq30aError
${ERROR_2}          id=lteq30bError
${SUBMIT_BUTTON}    css=[name="submitbutton"]
${CLEAR_BUTTON}     id=clear-rendered-form-results
${RESULTS}          id=rendered-form-results