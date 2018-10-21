Protocol
--------

.. seqdiag::
   :desctable:

   seqdiag {
      # On register
      Device ->  Instark [label = "POST /devices 
        {registration_token=123,
        channel_id=xyz}"];
      
      # On message
      Sender -> Instark [label = "POST /messages
        {type=device, reference=123, content}"];
      
      Instark -> Backend [label = "POST Messages Backend API
        {type=device, reference=123, content}"];
    
      Backend -> Device [label = "Mesage Delivery
        {content}"]
      
      Device [description = "Mobile or web device."];
      Instark [description = "Messaging Server."];
      Backend [description = "Infrastructure Backend."];
      Sender [description = "Sending Application"]
   }
