# Assignment1
#	 Monitoring a Kubernetes-Hosted Application Using SSO with Gmail, Syslog, Azure Log Analytics, #					and Grafana

## Team Members:

* Ahmad Sultan
* Akin Kuyga
* Chowdhurysal Ferdowsy
* Cameron Barber
* Jaehoandrew Han

## Steps are taken:

## 1. Application Setup in Kubernetes

### Objective: Deploy an application on Kubernetes that requires authentication and configure it to use Gmail for SSO authentication using OAuth 2.0.

*Assignment1 folder structure from VScode

![A screenshot of a computer Description automatically
generated](./Screenshots/1x.png)

### Steps:

* Choose an Application: For this assignment, we chose a To-Do Python app to use:

*app.py python application is created and tested, it is working:

![A screenshot of a computer Description automatically
generated](./Screenshots/1a1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1a2.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1a3.png)

* Containerize the Application: Created a Dockerfile, and build a Docker image.

* Docker file created, docket image deoployed and pushed to the hub. It is working:

![A screenshot of a computer Description automatically
generated](./Screenshots/1b1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1b2.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1b3.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1b4.png)

* Deploy on Kubernetes: Write a Kubernetes deployment YAML file to deploy application. This will include creating a deployment and a service to expose your application.

* Created kubernetes AKS from Porta and created yaml file. And then deployed.

![A screenshot of a computer Description automatically
generated](./Screenshots/1c1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1c2.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1c3.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1c31.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1c4.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/1c32.png)

* Configure SSO with Gmail: Implement OAuth 2.0 in the application to use Gmail for authentication.  Registered the application in Google Cloud Platform to get the necessary credentials (Client ID and Client Secret) and configure the redirect URIs.

* Creating API registration (credential) from the Google Cloud platform:

![A screenshot of a computer Description automatically
generated](./Screenshots/1d1.png)

* Use Google credentials on the Python app:

![A screenshot of a computer Description automatically
generated](./Screenshots/1d2.png)

## 2. Syslog Server Configuration

### Objective: Set up and configure a syslog server to capture events from the Kubernetes-hosted application.

### Steps:

* Syslog Server Setup: Choose a Syslog server solution (e.g., Syslog-NG, rsyslog) and deploy it either within the Kubernetes cluster as a pod or externally. 

* Created syslog-ng.yaml file and deployed, 

![A screenshot of a computer Description automatically
generated](./Screenshots/2a1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/2a2.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/2a3.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/2a4.png)

* Configure Log Forwarding: Modify the application's logging configuration to forward logs to the syslog server. 

![A screenshot of a computer Description automatically
generated](./Screenshots/2b1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/2b2.png)

## 3. Integration with Azure Log Analytics

### Objective: Configure the syslog server to push logs to Azure Log Analytics for storage and analysis.

### Steps:

* Create Azure Log Analytics Workspace: create a new workspace in Azure Log Analytics and Azure Monitor and then connect them our AKS cluster

![A screenshot of a computer Description automatically
generated](./Screenshots/3a0.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/3a.png)

* Configure Syslog Server: Set up the Syslog server to forward logs to Azure Log Analytics. 

![A screenshot of a computer Description automatically
generated](./Screenshots/3b.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/3c.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/3d.png)

* Ensure Proper Log Formatting: The logs sent to Azure Log Analytics are correctly formatted and include necessary information for effective monitoring.

![A screenshot of a computer Description automatically
generated](./Screenshots/3e.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/3e.png)

## 4. Data Visualization with Grafana

### Objective: Set up Grafana to visualize telemetry data from Azure Log Analytics.

### Steps:

* Set Up Grafana: Deploy Grafana and configure it to connect to your Azure Log Analytics workspace as a data source.

![A screenshot of a computer Description automatically
generated](./Screenshots/4a0.png

![A screenshot of a computer Description automatically
generated](./Screenshots/4a1.ng)

![A screenshot of a computer Description automatically
generated](./Screenshots/4a2.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/4a3.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/4a3.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/4a4.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/4a5.png)


* Create Dashboards: Design and create Grafana dashboards to visualize various telemetry data points from the application logs.

![A screenshot of a computer Description automatically
generated](./Screenshots/4b1.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/4c.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/FINAL.png)

![A screenshot of a computer Description automatically
generated](./Screenshots/FINAL2.png)


## Short Report:

We worked on setting up a to-do python app to run on Kubernetes, which is like a system that can manage lots of apps at once. We chose an app that can let people sign in using their Gmail accounts. To get this to work, we had to pack the app in a way that Kubernetes can use it, which is called containerization. Then, we wrote some instructions (in a YAML file) to tell Kubernetes how to run our app. 
After that, we set up a special server to collect all the messages (syslog) and errors from our app, so we can see if it's working right. We also connected this server to a tool called Azure Log Analytics, which keeps these messages safe and lets us look at them later. 
Then, we used Grafana, which is like a drawing tool for data, to make pictures and charts of what's happening in our app. This helps us understand how our app is doing. In the end, we wrote down all the steps we took, so we can remember how to do this again or show others how to do it. This project taught us how to get our app ready for Kubernetes, how to keep track of what it's doing, and how to make Grafana connection with Azure Monitor agent to understand our app better.





# 				Thank You!!!
