import logging
from flask import jsonify, Blueprint
from apis.utils import load_posts_from_json, get_post_by_pk


api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename='./logs/apis.log',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger()


@api_blueprint.route('/apis/posts', methods=['GET'])
def get_all_posts():
    logger.info('Запрос /apis/posts')
    return jsonify(load_posts_from_json())


@api_blueprint.route('/apis/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logger.info(f'Запрос /apis/posts/{postid}')
    return jsonify(get_post_by_pk(postid))
