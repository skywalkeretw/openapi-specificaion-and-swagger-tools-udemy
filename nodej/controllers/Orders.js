'use strict';

var utils = require('../utils/writer.js');
var Orders = require('../service/OrdersService');

module.exports.ordersDELETE = function ordersDELETE (req, res, next, orderId) {
  Orders.ordersDELETE(orderId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.ordersGET = function ordersGET (req, res, next, orderId) {
  Orders.ordersGET(orderId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.ordersPOST = function ordersPOST (req, res, next, body) {
  Orders.ordersPOST(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.ordersPUT = function ordersPUT (req, res, next, body) {
  Orders.ordersPUT(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
