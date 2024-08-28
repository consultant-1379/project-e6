package com.ericsson.springapi.repository;

import com.ericsson.springapi.model.Product;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ProductRepository extends MongoRepository<Product, String> {
}
