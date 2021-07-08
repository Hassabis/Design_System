# 最是人间留不住,朱颜辞镜花辞树
# -*- coding:utf-8 -*-
def jwt_response_payload_hendler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id': user.id,
        'birthday': user.birthday,
        'profession': user.profession,
        'gender':user.gender
    }
