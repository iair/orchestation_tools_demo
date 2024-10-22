# Orchestation tools evaluation

This a repo to understand how orchestation tools work. I will evaluate Luigi, Prefect and Dagster. Airflow was not evaluated because the learning curve was to high and the complexity of the project didn't require that kind of personalization and complexity on the orchestation tool.

## The working demo in the repo with Prefect

The demo was done with Prefect, as it outperforms Luigi in the capabilities we needed. The task done are:

1. Extract json data from a URL
2. Process that json data
3. Save the process data in a csv
4. Send me an email with the message of completed or failed using the Block

Everything was executed and monitored using Prefect Cloud and their interface:

![Captura de pantalla 2024-10-22 a la(s) 08 04 57](https://github.com/user-attachments/assets/736f77f6-a01d-4bf0-89f0-7fca7a729b61)


![Captura de pantalla 2024-10-22 a la(s) 08 03 32](https://github.com/user-attachments/assets/4e4c3201-1b4e-4f1c-82cf-91c3dbaf69f5)


![Captura de pantalla 2024-10-22 a la(s) 08 02 55](https://github.com/user-attachments/assets/cdabf98a-7165-48f5-bc15-da7a190c6978)


## The evaluation

### Creating our own framework to evaluate the tools

In this document we want to understand which is the best tool for our requirements. In order to do that, we did two things:

Ask several questions about the components and how the workflow works
Created a rubric to measure the alignment between our requirements and the capabilities of the tool

**Questions**

1. What is it? 
2. Which is the main purpose for which it was created?
3. Which are the main components?
4. How is it executed?
5. Has a visualization tool that enables us to monitor the pipeline (ideally with task graph)?
6. Do they save some records of the executions?
7. How is it triggered?
8. How reruns are handled?
9. Does it work in a local environment?
10. How is it deployed?
11. Where is it deployed?
12. Is it scalable?
13. Has Documentation?

**Rubric**

1. Execute task where the output of one task can be the input of another 
2. Being able to work on local environment for development
3. Has a simple and agnostic way to setup the deploy
4. Has implemented a way of tracking executions
5. Has a visualization tool that enable us to monitor the pipeline (ideally with task graph)
6. Has a scheduling function that i can configurate to program when to run?
7. it has a event based scheduling configuration?
8. It has a automatical re-run function that i can manipulate with rules on the configuration
9. It's possible to re-run a process base on the rules configurated by me for retry?
10. It's possible to re-run a process and only execute the task that failed?
11. Has a good documentation
12.  Easy to learn

## Summarize tables

#### With our evaluation and rubric

<img width="639" alt="Captura de pantalla 2024-10-22 a la(s) 08 11 40" src="https://github.com/user-attachments/assets/803c5a82-1f45-420f-865d-e1bcca12b6a6">

#### GPT evaluation

<img width="937" alt="Captura de pantalla 2024-10-22 a la(s) 08 10 18" src="https://github.com/user-attachments/assets/05a88592-577e-412d-9f42-2eb331bcdb61">

## Questions answered by tool

### Luigi

**Here are the answers for Luigi:**

1. **What is it?**  
   Luigi is a Python package used for building and managing complex data pipelines.

2. **Main purpose?**  
   It was created to handle long-running batch jobs and ensure that tasks are executed in the correct order.

3. **Main components?**  
   The main components are Tasks, Targets (outputs), and Workers.

4. **How is it executed?**  
   Luigi tasks are executed through a command-line interface using Python scripts

5. **Visualization tool?**  
   Yes, Luigi provides a web-based UI to monitor task pipelines.

6. **Save records of executions?**  
   Yes, Luigi saves the status of task executions.

7. **How is it triggered?**  
   Tasks are triggered by dependency resolution and scheduled execution. Luigi does not have a built-in, fully-featured scheduling system like Prefect. It relies on external schedulers, such as cron, to run workflows at specific intervals. Luigi can handle task dependencies and order of execution, but it requires something like cron to actually schedule when the pipeline or workflow should begin. 

8. **How reruns are handled**
   Luigi does not have an automatic re-run function with configurable rules. If a task fails, it will need to be rerun manually or with an external retry mechanism (like using cron jobs or external orchestration tools). However, Luigi can handle
   retries for tasks marked as failed when manually triggered, but there are no advanced rules for automatic retries like you might find in more modern orchestration tools such as Prefect or Airflow

9. **Work in local environment?**  
   Yes, it can be run locally.

10. **How is it deployed?**  
   Luigi can be deployed on local machines, clusters, or in the cloud, but requires manual configuration.

11. **Where is it deployed?**  
   It can be deployed on local servers or cloud-based environments.

12. **Scalable?**  
    Yes but not withouth effort. Luigi scales well across distributed systems, but it may require additional setup.

13. **Has Documentation?**  
    No, Luigi has comprehensive documentation available but for some reason i could not access directly to the details of each function, you can only do it putting the name of the function or some word in the search bar.

**In Luigi, the components interact as follows:**

- **Tasks**: The core units of work. Each task represents a single job (e.g., loading data).
- **Dependencies**: Tasks can have dependencies on other tasks, meaning they can only run once the required task completes.
- **Workers**: They manage task execution, ensuring the dependencies are resolved in order.
- **Targets**: Tasks generate output, referred to as a Target, which serves as input for dependent tasks.

### Prefect

**Here are the answers for Prefect:**

1. **What is it?**
   Prefect is a workflow orchestration tool that simplifies the execution and monitoring of data pipelines.

2. **Main purpose?**
   It was created to automate, orchestrate, and monitor workflows, ensuring resiliency, scalability, and ease of use in data pipelines.

3. **Main components?**
   Key components include Flows, Tasks, Agents, Workers, and Projects for defining, executing, and monitoring workflows.

4. **How is it executed?**
   Flows are executed using Prefect Agents or Workers, which run tasks in parallel.

5. **Visualization tool?**
   Yes, it includes a dashboard with a task graph for pipeline monitoring.

6. **Saves records?**
   Yes, Prefect records and logs every workflow execution.

7. **How is it triggered?**
   Triggers can be event-driven, schedule-based, or manually executed.

8. **How reruns are handled?**

9. **Works locally?**
   Yes, Prefect can run in local environments.

10. **How is it deployed?**
   Prefect can be deployed using Prefect Cloud, Docker, Kubernetes, or on a local server.

11. **Scalable?**
   Yes, it scales horizontally across distributed systems.

12. **Has Documentation?**
   Yes, comprehensive documentation is available on Prefect’s website.

**In Prefect, the components interact as follows:**

- **Flows**: These define the overall workflow and organize tasks.
- **Tasks**: Tasks represent individual units of work and are executed within a flow.
- **Agents**: Agents are responsible for deploying and running flows on specific infrastructure environments.
- **Workers**: Workers distribute the task execution, ensuring they run in parallel and on distributed systems.
- **Projects**: Projects group flows together, helping organize large-scale workflows.


## Bibliografía

**Official doc**

- Prefect: https://docs.prefect.io/3.0/get-started/index / https://www.prefect.io/blog#prefect-product
- Luigi: https://luigi.readthedocs.io/en/stable/index.html
- dagster: https://docs.dagster.io/getting-started?_gl=1*dogn49*_gcl_au*ODA0Mzg1NTI5LjE3MjIwMDQyMTU.*_ga*MTUzNzAxOTAxOS4xNzIwNzE4NDg1*_ga_84VRQZG7TV*MTcyOTUxODgzOS4xOC4xLjE3Mjk1MTkwMDEuNS4wLjA.

**Articles**

- https://medium.com/big-data-processing/getting-started-with-luigi-what-why-how-f8e639a1f2a5
- https://medium.com/@nitaionutandrei/workflow-orchestrators-airflow-vs-prefect-vs-dagster-0392b00dff30
- https://medium.com/dev-genius/orchestrate-modern-data-stack-with-dagster-0b6cf4d2d291
- https://dagster.io/vs/dagster-vs-prefect
