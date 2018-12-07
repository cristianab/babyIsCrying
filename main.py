import firebase_admin
from firebase_admin import db
import flask

firebase_admin.initialize_app(options={
    'databaseURL': 'https://babyiscrying-58c27.firebaseio.com',
})

NOTIFICATIONS = db.reference('updates')

def create_notification(request):
    req = request.json
    notification = NOTIFICATIONS.push(req)
    return flask.jsonify({'id': notification.key}), 201

def read_notification(id):
    notification = NOTIFICATIONS.child(id).get()
    if not notification:
        return 'Resource not found', 404
    return flask.jsonify(notification)

def update_notification(id, request):
    notification = NOTIFICATIONS.child(id).get()
    if not notification:
        return 'Resource not found', 404
    req = request.json
    NOTIFICATIONS.child(id).update(req)
    return flask.jsonify({'success': True})

def delete_notification(id):
    notification = NOTIFICATIONS.child(id).get()
    if not notification:
        return 'Resource not found', 404
    NOTIFICATIONS.child(id).delete()
    return flask.jsonify({'success': True})

def mainFunc(request):
    if request.path == '/' or request.path == '':
        if request.method == 'POST':
            return create_notification(request)
        else:
            return 'Method not supported', 405
    if request.path.startswith('/'):
        id = request.path.lstrip('/')
        if request.method == 'GET':
            return read_notification(id)
        elif request.method == 'DELETE':
            return delete_notification(id)
        elif request.method == 'PUT':
            return update_notification(id, request)
        else:
            return 'Method not supported', 405
    return 'URL not found', 404