package com.ericsson.springapi.service;

import com.ericsson.springapi.exceptions.ProductNotFoundException;
import com.ericsson.springapi.model.Product;
import com.ericsson.springapi.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;
import java.util.Set;

@Service
public class ProductServiceImpl implements ProductService {

    private ProductRepository productRepository;

    //  Redid field injection to be constructor injection for testing purposes
    @Autowired
    public ProductServiceImpl(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }


    @Override
    public Product getProductById(String id) {

        Optional<Product> productDb = this.productRepository.findById(id);

        if (productDb.isPresent()) {
            return productDb.get();
        } else {
            throw new ProductNotFoundException("Product not found with id : " + id);
        }

    }

    @Override
    public Set<String> findApplicationsInProduct(String id) {
        return getProductById(id).findApplications();
    }

    @Override
    public Set<String> findInstancesOfApplicationInProduct(String id, String application) {
        return getProductById(id).findInstancesInApplication(application);
    }

    @Override
    public Object findSpecificInstanceMetricsInProduct(String id, String application, String instance, String date) {
        return getProductById(id).findSpecificInstanceMetrics(application, instance, date);
    }

    @Override
    public Object findMetricsForEachInstanceInApplicationInProduct(String id, String application, String date) {
        return getProductById(id).findMetricsForEachInstanceInApplication(application, date);
    }

    @Override
    public Object findAllMetricsInProductInProduct(String id, String date) {
        return getProductById(id).findAllMetrics(date);
    }

}
