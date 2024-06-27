from twilio.rest import Client

def notificar(usuario):
    # Configuração do Twilio
    account_sid = 'ACa7f05d5b0c96f031ee4897724da93d40'
    auth_token = 'XXXXX'
    messaging_service_sid = 'MG13690eb74ab9c9e251bb119aa66ceb0a'
    whatsapp_number = 'whatsapp:+556136863228'
    client = Client(account_sid, auth_token)

    # Cria a mensagem com os dados da linha atual
    message_body = f'O {usuario} solicitou retorno de urgência.'

    # Envia a mensagem pelo Twilio (SMS)
    message = client.messages.create(
        messaging_service_sid=messaging_service_sid,
        body=message_body,
        to='+5561993376654'
    )

    # Envia a mensagem pelo Twilio (SMS)
    message = client.messages.create(
        messaging_service_sid=messaging_service_sid,
        body=message_body,
        to='+5561992807020'
    )

    # Envia a mensagem pelo Twilio (SMS)
    message = client.messages.create(
        messaging_service_sid=messaging_service_sid,
        body=message_body,
        to='+5561993352351'
    )

    # Envia a mensagem pelo Twilio (WhatsApp)
    whatsapp_body = f'O {usuario} solicitou retorno de urgência.'
    message_whatsapp = client.messages.create(
        from_=whatsapp_number,
        body=whatsapp_body,
        to='whatsapp:+556193376654'
    )

    # Envia a mensagem pelo Twilio (WhatsApp)
    message_whatsapp = client.messages.create(
        from_=whatsapp_number,
        body=whatsapp_body,
        to='whatsapp:+556192807020'
    )

    # Envia a mensagem pelo Twilio (WhatsApp)
    message_whatsapp = client.messages.create(
        from_=whatsapp_number,
        body=whatsapp_body,
        to='whatsapp:+556193352351'
    )
