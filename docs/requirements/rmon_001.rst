Requirement 001
-------------
    Sending messages by different protocols

User History
^^^^^^^^^^^^
    * How: User.
    * Want: According to the data to be sent, it is required to choose a protocol to reach the device.   
    * for: Centralize in a service the sending of datas with different protocols.

Validation Criteria
^^^^^^^^^^^^^^^^^^^

Criterion 1
^^^^^^^^^^^
    * Given: That this service need send mails, text messages and other data.
    * When: One aplication required send information by a protocol specific.
    * Then: The service choose the protocol.

Criterion 2
^^^^^^^^^^^
    * Given: That this service need identify if the device have a channel or not.
    * When: Before to send the data.
    * Then: The service choose if data is group or direct message.