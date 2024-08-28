package com.ericsson.springapi.service;

import com.ericsson.springapi.model.Product;

import java.util.Set;

public interface ProductService {

    Product getProductById(String id);

    Set<String> findApplicationsInProduct(String id);

    Set<String> findInstancesOfApplicationInProduct(String id, String application);

    Object findSpecificInstanceMetricsInProduct(String id, String application, String instance, String date);

    Object findMetricsForEachInstanceInApplicationInProduct(String id, String application, String date);

    Object findAllMetricsInProductInProduct(String id, String date);

}
