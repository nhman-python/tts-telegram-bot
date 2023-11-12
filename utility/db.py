import time
from .logs import logger

import redis

MESSAGE_LIMIT = 4
TIME_WINDOW = 300


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def user_logger(user_id):
    if not redis_client.get(user_id):
        redis_client.set(user_id, time.time())
        logger.info(f"New user {user_id} logged.")


def check_message_limit(user_id):
    key = f"message_limit:{user_id}"
    current_count = redis_client.get(key)
    return not current_count or int(current_count) < MESSAGE_LIMIT


def update_message_count(user_id):
    key = f"message_limit:{user_id}"
    redis_client.incr(key)
    redis_client.expire(key, TIME_WINDOW)


def is_user_block(user_id):
    key = f"user_block:{user_id}"
    return redis_client.get(key)


def block_user(user_id):
    key = f"user_block:{user_id}"
    return redis_client.set(key, '1')
