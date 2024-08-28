import React, { useState } from 'react';
import './App.css';



const searchMetricsForm1 = (
    product, setProduct, 
    date, setDate,
    handleFindingMetrics) => {
    return (
        <div>
            <form>
                <h1>Metrics Form 1</h1>
                <label>
                    <input 
                        value={product}   
                        name="product"
                        autoComplete="nope"
                        placeholder="Product"
                        onChange={e => setProduct(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={date}   
                        name="date"
                        autoComplete="nope"
                        placeholder="dd-mm-yyyy"
                        onChange={e => setDate(e.target.value)} 
                    />
                </label>
            </form>
            <button onClick={() => handleFindingMetrics()}>search</button>
        </div>
    )
}

const searchMetricsForm2 = (
    product, setProduct, 
    date, setDate,
    application, setApplication,
    handleFindingMetrics) => {
    return (
        <div>
            <form>
                <h1>Metrics Form 2</h1>
                <label>
                    <input 
                        value={product}   
                        name="product"
                        autoComplete="nope"
                        placeholder="Product"
                        onChange={e => setProduct(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={date}   
                        name="date"
                        autoComplete="nope"
                        placeholder="dd-mm-yyyy"
                        onChange={e => setDate(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={application}   
                        name="application"
                        autoComplete="nope"
                        placeholder="Application"
                        onChange={e => setApplication(e.target.value)} 
                    />
                </label>
            </form>
            <button onClick={() => handleFindingMetrics()}>search</button>
        </div>
    )
}

const searchMetricsForm3 = (
    product, setProduct, 
    date, setDate,
    application, setApplication,
    instance, setInstance,
    handleFindingMetrics) => {
    return (
        <div>
            <form>
                <h1>Metrics Form 3</h1>
                <label>
                    <input 
                        value={product}   
                        name="product"
                        autoComplete="nope"
                        placeholder="Product"
                        onChange={e => setProduct(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={date}   
                        name="date"
                        autoComplete="nope"
                        placeholder="dd-mm-yyyy"
                        onChange={e => setDate(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={application}   
                        name="application"
                        autoComplete="nope"
                        placeholder="Application"
                        onChange={e => setApplication(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={instance}   
                        name="instance"
                        autoComplete="nope"
                        placeholder="Instance"
                        onChange={e => setInstance(e.target.value)} 
                    />
                </label>
            </form>
            <button onClick={() => handleFindingMetrics()}>search</button>
        </div>
    )
}

const findApplications = (
    product, setProduct,
    handleFindingMetrics) => {
    return (
        <div>
            <form>
                <h1>Find Applications Form</h1>
                <label>
                    <input 
                        value={product}   
                        name="product"
                        autoComplete="nope"
                        placeholder="Product"
                        onChange={e => setProduct(e.target.value)} 
                    />
                </label>
            </form>
            <button onClick={() => handleFindingMetrics()}>search</button>
        </div>
    )
}

const findInstances = (
    product, setProduct, 
    application, setApplication,
    handleFindingMetrics) => {
    return (
        <div>
            <form>
                <h1>Find Instances in Application Form</h1>
                <label>
                    <input 
                        value={product}   
                        name="product"
                        autoComplete="nope"
                        placeholder="Product"
                        onChange={e => setProduct(e.target.value)} 
                    />
                    <br></br>
                    <input 
                        value={application}   
                        name="application"
                        autoComplete="nope"
                        placeholder="Application"
                        onChange={e => setApplication(e.target.value)} 
                    />
                </label>
            </form>
            <button onClick={() => handleFindingMetrics()}>search</button>
        </div>
    )
}

const metricsTable = (data, instance) => {
    if (data[instance] !== null) {
        return (
            <tr key={instance}>
                <td>{instance}</td>
                <td>{data[instance].Total_Logs}</td>
                <td>{data[instance].Total_Errors}</td>
                <td>{data[instance].Total_Warning}</td>
                <td>{data[instance].Total_Info}</td>
                <td>{data[instance].Duplicates}</td>
                <td>{data[instance].Missing_Msg}</td>
            </tr>
        )
    }
}

const SortByTotalLogs = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            return parseInt(data[application1].Total_Logs) - parseInt(data[application2].Total_Logs)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const SortByErrors = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            return parseInt(data[application1].Total_Errors) - parseInt(data[application2].Total_Errors)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const SortByWarnings = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            return parseInt(data[application1].Total_Warning) - parseInt(data[application2].Total_Warning)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const SortByInfo = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            return parseInt(data[application1].Total_Info) - parseInt(data[application2].Total_Info)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const SortByDuplicates = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            return parseInt(data[application1].Duplicates) - parseInt(data[application2].Duplicates)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const SortByMissingMsg = (data) => {
    if (Object.values(data)[0] !== null) {
        return Object.keys(data).sort((application1, application2) => {
            console.log("loop")
            return parseInt(data[application1].Missing_Msg) - parseInt(data[application2].Missing_Msg)
        }).reverse().map((instance) => {
            return metricsTable(data, instance)
        })
    }
}

const noSort = (data) => {
    return Object.keys(data).map((instance) => {
        return metricsTable(data, instance)
    })
}

const App = () => {

    const [data, setData] = useState([])
    const [metricsSearch, setMetricsSearch] = useState(true)
    const [currentForm, setcurrentForm] = useState("metrics form 2")
    const [title, setTitle] = useState("Metrics")

    // user inputs
    const [product, setProduct] = useState("LMI_KOHN017")
    const [application, setApplication] = useState("eric-oss-sftp-filetrans")
    const [instance, setInstance] = useState("eric-oss-sftp-filetrans-03")
    const [date, setDate] = useState("31-07-2023")

    // choosing form
    const handleFormToggle = (form) => {
        setcurrentForm(form)
    }

    // metrics related functionality
    const [sortLogsBy, setSortLogsBy] = useState()

    const handleSort = (metric) => {
        setSortLogsBy(metric)
    }

    // using spring API for finding existing instances and applications
    const handleFindingApplicationInProduct = async () => {
        
        setData([])
        setMetricsSearch(false)

        try {
            var uri = "http://localhost:8080/products/" + product + "/applications"
            fetch(uri)
            .then(res=>res.json())
            .then((result)=>{
                setData(result);
                setTitle("Applications in " + product)
            })
        } catch (e) {
            console.log(e)
        }

        
    }

    const handleFindingInstancesInApplication = async () => {

        setData([])
        setMetricsSearch(false)

        var uri = "http://localhost:8080/products/" + product + "/" + application + "/instances"
        fetch(uri)
        .then(res=>res.json())
        .then((result)=>{
            setData(result);
            setTitle("Instances in " + product + "/" + application)
        })
    }

    // using spring API for finding metrics
    const handleFindingMetricsForEveryApplicationInProduct = async () => {

        setData([])
        setMetricsSearch(true)

        try {
            var uri = "http://localhost:8080/products/" + product + "/metrics/" + date
            fetch(uri)
            .then(res=>res.json())
            .then((result)=>{
                setData(result);
                setTitle("Metrics: " + product)
            })
        } catch (e) {
            setData([])
        }
        
    }

    const handleFindingMetricsForInstancesInApplication = async () => {

        setData([])
        setMetricsSearch(true)

        var uri = "http://localhost:8080/products/" + product + "/" + application + "/metrics/" + date
        fetch(uri)
        .then(res=>res.json())
        .then((result)=>{
            setData(result);
            setTitle("Metrics: " + product + ">" + application)
        })
    }

    const handleFindingMetricsForSpecificInstance = async () => {

        setMetricsSearch(true)
        setTitle("Metrics: " + product + ">" + application + ">" + instance)

        var uri = "http://localhost:8080/products/" + product + "/" + application + "/" + instance + "/" + date
        fetch(uri)
        .then(res=>res.json())
        .then((result)=>{
            setData(result);
        }) 
    }
    
    return (
        <><div className="App">
            <div>
                <button onClick={() => handleFormToggle("metrics form 1")}>All Metrics</button>
                <button onClick={() => handleFormToggle("metrics form 2")}>Metrics for Application</button>
                <button onClick={() => handleFormToggle("metrics form 3")}>Metrics for specific Instance</button>
                <button onClick={() => handleFormToggle("applications form")}>Find Applications</button>
                <button onClick={() => handleFormToggle("instances form")}>Find Instances</button>
                <button onClick={() => handleFormToggle("hide")}>Hide Form</button>
            </div>
            {
                currentForm === "metrics form 1"? 
                (searchMetricsForm1(
                    product, setProduct, 
                    date, setDate, 
                    handleFindingMetricsForEveryApplicationInProduct
                )) : currentForm === "metrics form 2"? 
                (searchMetricsForm2(
                    product, setProduct, 
                    date, setDate, 
                    application, setApplication,
                    handleFindingMetricsForInstancesInApplication
                )) : currentForm === "metrics form 3"? 
                (searchMetricsForm3(
                    product, setProduct, 
                    date, setDate, 
                    application, setApplication,
                    instance, setInstance,
                    handleFindingMetricsForSpecificInstance
                )) : currentForm === "applications form"? 
                (findApplications(
                    product, setProduct,
                    handleFindingApplicationInProduct
                )) : currentForm === "instances form"?
                (findInstances(
                    product, setProduct,
                    application, setApplication,
                    handleFindingInstancesInApplication
                )) : null

            }
            {
                metricsSearch? (
                    <div>
                        <h1>{title}</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th>Instance</th>
                                    <th onClick={() => handleSort("total logs")}>Total Logs</th>
                                    <th onClick={() => handleSort("errors")}>Errors</th>
                                    <th onClick={() => handleSort("warnings")}>Warnings</th>
                                    <th onClick={() => handleSort("info")}>Info</th>
                                    <th onClick={() => handleSort("duplicates")}>Duplicates</th>
                                    <th onClick={() => handleSort("missing msg")}>Missing Messages</th>    
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    sortLogsBy === "total logs"?  
                                        (SortByTotalLogs(data)) : sortLogsBy === "errors"?
                                        (SortByErrors(data)) : sortLogsBy === "warnings"? 
                                        (SortByWarnings(data)) : sortLogsBy === "info"? 
                                        (SortByInfo(data)) : sortLogsBy === "duplicates"? 
                                        (SortByDuplicates(data)) : sortLogsBy === "missing msg"?
                                        (SortByMissingMsg(data)) : (noSort(data))
                                }
                            </tbody>
                        </table>
                    </div>
                ) : (
                    <div>
                        <h1>{title}</h1>
                        <table>
                            <thead>
                                <tr><th></th></tr>
                            </thead>
                            <tbody>
                                {
                                    data.map((item) => {
                                        return (
                                            <tr key={item}>
                                                <td>{item}</td>
                                            </tr>
                                        )
                                    })
                                } 
                            </tbody>
                        </table>
                    </div>
                )
            }
            
        </div></>
    );
}

export default App;