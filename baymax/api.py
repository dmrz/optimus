import json

import aiohttp


async def request(url, payload=None, params=None, headers=None):
    headers = {'content-type': 'application/json', **(headers or {})}
    data = payload and json.dumps(payload)
    async with aiohttp.ClientSession() as client:
        async with client.post(
                url, data=data, params=params, headers=headers) as resp:
            # TODO: Check response status
            json_response = await resp.json()
            return json_response


async def get_updates(base_url, timeout, offset):
    params = {
        'timeout': timeout,
        'offset': offset
    }
    return await request(f'{base_url}/getUpdates', params=params)


async def get_me(base_url):
    return await request(f'{base_url}/getMe')


async def send_message(
        base_url, chat_id, text,
        parse_mode=None, disable_web_page_preview=None,
        disable_notification=None, reply_to_message_id=None,
        reply_markup=None):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    if parse_mode is not None:
        # TODO: Implement setting of a parse mode to payload
        pass
    if disable_web_page_preview is not None:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id is not None:
        payload['reply_to_message_id'] = reply_to_message_id
    if reply_markup is not None:
        payload['reply_markup'] = reply_markup
    return await request(f'{base_url}/sendMessage', payload)


async def forward_message(
        base_url, chat_id, from_chat_id,
        message_id, disable_notification=None):
    payload = {
        'chat_id': chat_id,
        'from_chat_id': from_chat_id,
        'message_id': message_id
    }
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    return await request(f'{base_url}/forwardMessage', payload)


async def answer_callback_query(
        base_url, callback_query_id, text, show_alert,
        url=None, cache_time=None):
    payload = {
        'callback_query_id': callback_query_id,
        'text': text,
        'show_alert': show_alert
    }
    if url is not None:
        payload['url'] = url
    if cache_time is not None:
        payload['cache_time'] = cache_time
    return await request(f'{base_url}/answerCallbackQuery', payload)
