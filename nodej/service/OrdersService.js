'use strict';


/**
 * Delete Order
 * Delete order details from EazyShop
 *
 * orderId Integer 
 * no response value expected for this operation
 **/
exports.ordersDELETE = function(orderId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Get Order Details
 * Get order details from EazyShop
 *
 * orderId Integer 
 * returns inline_response_200
 **/
exports.ordersGET = function(orderId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "address" : {
    "zipcode" : "zipcode",
    "city" : "city",
    "state" : "California",
    "addressLine" : "addressLine",
    "isOfficeAddress" : true
  },
  "orderId" : 0,
  "products" : [ {
    "quantity" : 1,
    "productId" : 0,
    "releaseDate" : "2000-01-23",
    "price" : 6.0274563,
    "name" : "name",
    "categoryName" : "categoryName"
  }, {
    "quantity" : 1,
    "productId" : 0,
    "releaseDate" : "2000-01-23",
    "price" : 6.0274563,
    "name" : "name",
    "categoryName" : "categoryName"
  } ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Create Order
 * Post order details to EazyShop for processing and shipping 
 *
 * body Orders_body_1  (optional)
 * returns inline_response_201
 **/
exports.ordersPOST = function(body) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "orderId" : 0
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update Order
 * Update order details to EazyShop for processing and shipping 
 *
 * body Orders_body  (optional)
 * no response value expected for this operation
 **/
exports.ordersPUT = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

