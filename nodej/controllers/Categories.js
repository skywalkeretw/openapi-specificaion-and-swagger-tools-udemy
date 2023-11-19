'use strict';

var utils = require('../utils/writer.js');
var Categories = require('../service/CategoriesService');

module.exports.categoriesCategoryIdGET = function categoriesCategoryIdGET (req, res, next, categoryId) {
  Categories.categoriesCategoryIdGET(categoryId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.categoriesGET = function categoriesGET (req, res, next, categoryId) {
  Categories.categoriesGET(categoryId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
