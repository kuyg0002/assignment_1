# Assignment1
#	 Monitoring a Kubernetes-Hosted Application Using SSO with Gmail, Syslog, Azure Log Analytics, #					and Grafana

## Team Members:

* Ahmad Sultan
* Akin Kuyga
* Chowdhurysal Ferdowsy
* Cameron Barbar
* Jaehoandrew Han

## Steps are taken:

## 1. Application Setup in Kubernetes

### Objective: Deploy an application on Kubernetes that requires authentication and configure it to use Gmail for SSO authentication using OAuth 2.0.

*Assignment1 folder structure from VScode

![A screenshot of a computer Description automatically
generated](./Screenshots/1x.png){width="6.5in" height="3.89375in"}

### Steps:

* Choose an Application: For this assignment we chose To-Do Python app to use:

*app.py python application is created and tested, it is working:

![A screenshot of a computer Description automatically
generated](./Screenshots/1a1.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1a2.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1a3.png){width="6.5in" height="3.89375in"}

* Containerize the Application: Created a Dockerfile, and build a Docker image.

* Docker file created, docket image deoployed and pushed to the hub. It is working:

![A screenshot of a computer Description automatically
generated](./Screenshots/1b1.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1b2.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1b3.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1b4.png){width="6.5in" height="3.89375in"}

* Deploy on Kubernetes: Write a Kubernetes deployment YAML file to deploy application. This will include creating a deployment and a service to expose your application.

* Created kubernetes AKS from Porta and created yaml file. And then deployed.

![A screenshot of a computer Description automatically
generated](./Screenshots/1c1.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1c2.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1c3.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1c31.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1c4.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/1c32.png){width="6.5in" height="3.89375in"}

* Configure SSO with Gmail: Implement OAuth 2.0 in application to use Gmail for authentication.  Registered the application in Google Cloud Platform to get the necessary credentials (Client ID and Client Secret) and configure the redirect URIs.

* Creating api registration (credential) from google cloud platform:

![A screenshot of a computer Description automatically
generated](./Screenshots/1d1.png){width="6.5in" height="3.89375in"}

* Use google credentials on the Python app:

![A screenshot of a computer Description automatically
generated](./Screenshots/1d2.png){width="6.5in" height="3.89375in"}

## 2. Syslog Server Configuration

### Objective: Set up and configure a syslog server to capture events from the Kubernetes-hosted application.

### Steps:

* Syslog Server Setup: Choose a syslog server solution (e.g., Syslog-NG, rsyslog) and deploy it either within the Kubernetes cluster as a pod or externally. 

* Created syslog-ng.yaml file and deployed, 

![A screenshot of a computer Description automatically
generated](./Screenshots/2a1.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/2a2.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/2a3.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/2a4.png){width="6.5in" height="3.89375in"}

* Configure Log Forwarding: Modify application's logging configuration to forward logs to the syslog server. 

![A screenshot of a computer Description automatically
generated](./Screenshots/2b1.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/2b2.png){width="6.5in" height="3.89375in"}

## 3. Integration with Azure Log Analytics

### Objective: Configure the syslog server to push logs to Azure Log Analytics for storage and analysis.

### Steps:

* Create Azure Log Analytics Workspace: create a new workspace in Azure Log Analytics.

![A screenshot of a computer Description automatically
generated](./Screenshots/3a.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/3a.png){width="6.5in" height="3.89375in"}

* Configure Syslog Server: Set up the syslog server to forward logs to Azure Log Analytics. 

![A screenshot of a computer Description automatically
generated](./Screenshots/3c.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/3d.png){width="6.5in" height="3.89375in"}

* Ensure Proper Log Formatting: The logs sent to Azure Log Analytics are correctly formatted and include necessary information for effective monitoring.

![A screenshot of a computer Description automatically
generated](./Screenshots/3e.png){width="6.5in" height="3.89375in"}

## 4. Data Visualization with Grafana

### Objective: Set up Grafana to visualize telemetry data from Azure Log Analytics.

### Steps:

* Set Up Grafana: Deploy Grafana and configure it to connect to your Azure Log Analytics workspace as a data source.

![A screenshot of a computer Description automatically
generated](./Screenshots/4a.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/4b.png){width="6.5in" height="3.89375in"}

* Create Dashboards: Design and create Grafana dashboards to visualize various telemetry data points from the application logs.

![A screenshot of a computer Description automatically
generated](./Screenshots/4c.png){width="6.5in" height="3.89375in"}

![A screenshot of a computer Description automatically
generated](./Screenshots/4d.png){width="6.5in" height="3.89375in"}

# Thank You!!!
