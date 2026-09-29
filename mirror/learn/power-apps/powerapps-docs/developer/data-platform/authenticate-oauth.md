---
layout: Conceptual
title: Use OAuth authentication with Microsoft Dataverse (Dataverse) - Power Apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
uhfHeaderId: MSDocsHeader-MSPowerApps
breadcrumb_path: ../../breadcrumb/toc.json
ms.suite: office
feedback_system: Standard
feedback_product_url: https://ideas.powerapps.com
recommendations: true
bilingual_type: hover over
learn_banner_products:
- powerapps
ms.topic: how-to
ms.service: powerapps
ms.subservice: dataverse-developer
search.app:
- PowerApps
- powerapps-docs
- dataverse-docs
description: Learn how to authenticate applications with Microsoft Dataverse using OAuth.
ms.custom: has-adal-ref
ms.date: 2026-07-24T00:00:00.0000000Z
ms.reviewer: pehecke
author: ritesp
ms.author: ritesp
search.audienceType:
- developer
contributors:
- JimDaly
locale: en-us
document_id: a7f57df6-59af-6e22-44d2-bc9bb1ee69c7
document_version_independent_id: fdce23ee-733d-bf3a-25c8-2ca6bfa8c852
original_content_git_url: https://github.com/MicrosoftDocs/powerapps-docs-pr/blob/live/powerapps-docs/developer/data-platform/authenticate-oauth.md
site_name: Docs
depot_name: MSDN.powerapps-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerapps-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: developer/data-platform/authenticate-oauth
moniker_range_name: 
monikers: []
item_type: Content
source_path: powerapps-docs/developer/data-platform/authenticate-oauth.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/0ceb3227-2ff7-4d97-8e75-3d7b9ccc937a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e31b9be-b6e9-4221-a20b-d1460dbd5dfa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4d680e1a-c470-4772-a236-5c714bd09be0
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/8d63a4c4-4889-43b4-a98e-8e50dbfdb083
platformId: 33b124fe-ee2c-31ef-cbbb-181505bff581
---

# Use OAuth authentication with Microsoft Dataverse (Dataverse) - Power Apps | Microsoft Learn

[OAuth 2.0](https://oauth.net/2/) is the industry-standard protocol for authorization. After application users provide credentials to authenticate, OAuth determines whether they're authorized to access the resources.

Client applications must support the use of OAuth to access data by using the Web API. OAuth enables two-factor authentication (2FA) or certificate-based authentication for server-to-server application scenarios.

OAuth requires an identity provider for authentication. For Dataverse, the identity provider is Microsoft Entra ID. To authenticate by using a Microsoft work or school account, use the [Microsoft Authentication Library](/en-us/azure/active-directory/develop/msal-overview#languages-and-frameworks) (MSAL).

Note

This article introduces common concepts related to connecting to Dataverse by using OAuth with authentication libraries. This content focuses on how a developer can connect to Dataverse but doesn't cover the inner workings of OAuth or the libraries. For complete information related to authentication, see the Microsoft Entra ID documentation. The article [What is authentication?](/en-us/azure/active-directory/develop/authentication-scenarios) is a good place to start.

The samples we provide are preconfigured with appropriate registration values so that you can run them without generating your own app registration. When you publish your own apps, you must use your own registration values.

## App registration

When you connect by using OAuth, you must first register an application in your Microsoft Entra ID tenant. How you register your app depends on the type of app you want to make.

In all cases, start with the basic steps to register an app described in the article: [Quickstart: Register an application with the Microsoft identity platform](/en-us/azure/active-directory/develop/quickstart-register-app). For Dataverse specific instructions, see [Walkthrough: Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory).

The decisions you need to make in this step mostly depend on the Application Type choice (see next section).

### Types of app registration

When you register an app with Microsoft Entra ID, choose the application type. You can register two types of applications:

| Application type | Description |
| --- | --- |
| Web app /API | **Web client**A type of [client application](/en-us/azure/active-directory/develop/developer-glossary#client-application) that executes all code on a web server.**User-agent-based client**A type of [client application](/en-us/azure/active-directory/develop/developer-glossary#client-application) that downloads code from a web server and executes within a user-agent (for instance, a web browser), such as a Single Page Application (SPA). |
| Native | A type of [client application](/en-us/azure/active-directory/develop/developer-glossary#client-application) that is installed natively on a device. |

When you select **Web app /API**, enter a **Sign-On URL**. Microsoft Entra ID sends the authentication response to this URL, including a token if authentication is successful. While you develop an app, set this URL to `https://localhost/appname:[port]` so you can develop and debug your app locally. When you publish your app, change this value to the published URL of the app.

When you select **Native**, enter a Redirect URI. This URL is a unique identifier to which Microsoft Entra ID redirects the user-agent in an OAuth 2.0 request. This URL is typically a value formatted like so: `app://<guid>`.

### Giving access to Dataverse

If your app is a client that allows the authenticated user to perform operations, configure the application to have the **Access Dynamics 365 as organization users** delegated permission.

For specific steps to set permissions, see [Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory).

If your app uses Server-to-Server (S2S) authentication, you don't need to complete this step. That configuration requires a specific system user and the operations performed by that user account rather than any user that must be authenticated.

### Use client secrets and certificates

For server-to-server scenarios, there's no interactive user account to authenticate. In these cases, you need to provide some means to confirm that the application is trusted. Confirm trust by using client secrets or certificates.

For apps that you register by using the **Web app /API** application type, you can configure secrets. Set these secrets in the **Keys** area under **API Access** in the **Settings** for the app registration.

For either application type, you can upload a certificate.

More information: Connect as an app

## Use authentication libraries to connect

Use one of the Microsoft-supported Microsoft Entra ID authentication client libraries to connect to Dataverse, such as the [Microsoft Authentication Library (MSAL)](/en-us/azure/active-directory/develop/reference-v2-libraries). This library is available for various platforms as described in the provided links.

Note

Microsoft Authentication Library (ADAL) isn't actively receiving updates and is supported only until June 2022. Use MSAL as the authentication library for projects.

For a code sample that demonstrates use of MSAL libraries for authentication with Dataverse, see [Quick start: Web API sample (C#)](webapi/quick-start-console-app-csharp).

### .NET client libraries

Dataverse supports application authentication with the Web API endpoint by using the OAuth 2.0 protocol. For your custom .NET applications, use MSAL for application authentication by using the Web API endpoint.

Dataverse SDK for .NET includes client classes [CrmServiceClient](/en-us/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) and [ServiceClient](/en-us/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient) to handle authentication. The `CrmServiceClient` class currently uses ADAL for authentication while `ServiceClient` uses MSAL. Writing your application code to use these clients removes the need to manage authentication directly. Both clients work with the SDK and Web API endpoints.

## Use the AccessToken with your requests

The point of using the authentication libraries is to get an access token that you can include with your requests. Getting the token only requires a few lines of code, and just a few more lines to configure an [HttpClient](/en-us/dotnet/api/system.net.http.httpclient) to execute a request.

Important

As demonstrated in the sample code of this article, use a "&lt;environment-url&gt;/user\_impersonation" scope for a public client. For a confidential client, use a scope of "&lt;environment-url&gt;/.default".

### Simple example

The following example is the minimum amount of code needed to execute a single Web API request, but it isn't the recommended approach. The example code uses the MSAL library and is taken from the [Quick start: Web API sample (C#)](webapi/quick-start-console-app-csharp) sample.

```csharp
string resource = "https://contoso.api.crm.dynamics.com";
var clientId = "51f81489-12ee-4a9e-aaae-a2591f45987d";
var redirectUri = "http://localhost"; // Loopback for the interactive login.

// MSAL authentication
var authBuilder = PublicClientApplicationBuilder.Create(clientId)
    .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
    .WithRedirectUri(redirectUri)
    .Build();
var scope = resource + "/user_impersonation";
string[] scopes = { scope };

AuthenticationResult token =
    authBuilder.AcquireTokenInteractive(scopes).ExecuteAsync().Result;

// Set up the HTTP client
var client = new HttpClient
{
    BaseAddress = new Uri(resource + "/api/data/v9.2/"),
    Timeout = new TimeSpan(0, 2, 0)  // Standard two minute timeout.
};

HttpRequestHeaders headers = client.DefaultRequestHeaders;
headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
headers.Add("OData-MaxVersion", "4.0");
headers.Add("OData-Version", "4.0");
headers.Accept.Add(
    new MediaTypeWithQualityHeaderValue("application/json"));

// Web API call
var response = client.GetAsync("WhoAmI").Result;
```

This simple approach doesn't represent a good pattern to follow because the `token` expires in about an hour. MSAL libraries cache the token for you and refresh it each time the `AcquireTokenInteractive` method is called. However in this simple example, the token is only acquired once.

### Example demonstrating a delegating message handler

Implement a class derived from [DelegatingHandler](/en-us/dotnet/api/system.net.http.delegatinghandler) and pass it to the constructor of [HttpClient](/en-us/dotnet/api/system.net.http.httpclient). By using this handler, you can override the [HttpClient](/en-us/dotnet/api/system.net.http.httpclient).[SendAsync](/en-us/dotnet/api/system.net.http.httpclient.sendasync) method so that the access token is refreshed by the `AcquireToken*` method calls with each request sent by the Http client.

The following code is an example of a custom class derived from [DelegatingHandler](/en-us/dotnet/api/system.net.http.delegatinghandler). This code is taken from the [Enhanced QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/EnhancedQuickStart) sample that uses the MSAL authentication library.

```csharp
class OAuthMessageHandler : DelegatingHandler
{
    private AuthenticationHeaderValue authHeader;
    public OAuthMessageHandler(string serviceUrl, string clientId, string redirectUrl, string username, string password,
            HttpMessageHandler innerHandler)
        : base(innerHandler)
    {
        string apiVersion = "9.2";
        string webApiUrl = $"{serviceUrl}/api/data/v{apiVersion}/";
        var authBuilder = PublicClientApplicationBuilder.Create(clientId)
                        .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
                        .WithRedirectUri(redirectUrl)
                        .Build();
        var scope = serviceUrl + "/user_impersonation";
        string[] scopes = { scope };
        // First try to get an authentication token from the cache using a hint.
        AuthenticationResult authBuilderResult=null;
        try
        {
            authBuilderResult = authBuilder.AcquireTokenSilent(scopes, username)
               .ExecuteAsync().Result;
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine(
                $"Error acquiring auth token from cache:{System.Environment.NewLine}{ex}");
            // Token cache request failed, so request a new token.
            try
            {
                if (username != string.Empty && password != string.Empty)
                {
                    // Request a token based on username/password credentials.
                    authBuilderResult = authBuilder.AcquireTokenByUsernamePassword(scopes, username, password)
                                .ExecuteAsync().Result;
                }
                else
                {
                    // Prompt the user for credentials and get the token.
                    authBuilderResult = authBuilder.AcquireTokenInteractive(scopes)
                                .ExecuteAsync().Result;
                }
            }
            catch (Exception msalex)
            {
                System.Diagnostics.Debug.WriteLine(
                    $"Error acquiring auth token with user credentials:{System.Environment.NewLine}{msalex}");
                throw;
            }
        }
        //Note that an Microsoft Entra ID access token has finite lifetime, default expiration is 60 minutes.
        authHeader = new AuthenticationHeaderValue("Bearer", authBuilderResult.AccessToken);
    }

    protected override Task<HttpResponseMessage> SendAsync(
              HttpRequestMessage request, System.Threading.CancellationToken cancellationToken)
    {
        request.Headers.Authorization = authHeader;
        return base.SendAsync(request, cancellationToken);
    }
}
```

When you use this `OAuthMessageHandler` class, the simple `Main` method looks like this.

```csharp
class Program
{
    static void Main(string[] args)
    {
        try
        {
            //Get configuration data from App.config connectionStrings
            string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;

            using (HttpClient client = SampleHelpers.GetHttpClient(connectionString, SampleHelpers.clientId,
                SampleHelpers.redirectUrl))
            {
                // Use the WhoAmI function
                var response = client.GetAsync("WhoAmI").Result;

                if (response.IsSuccessStatusCode)
                {
                    //Get the response content and parse it.
                    JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
                    Guid userId = (Guid)body["UserId"];
                    Console.WriteLine("Your UserId is {0}", userId);
                }
                else
                {
                    Console.WriteLine("The request failed with a status of '{0}'",
                                response.ReasonPhrase);
                }
                Console.WriteLine("Press any key to exit.");
                Console.ReadLine();
            }
        }
        catch (Exception ex)
        {
            SampleHelpers.DisplayException(ex);
            Console.WriteLine("Press any key to exit.");
            Console.ReadLine();
        }
    }
}
```

Read the following important information about using a connection string or username/password authentication in application code.

Important

Microsoft recommends that you use the most secure authentication flow available. The authentication flow described in this article requires a very high degree of trust in the application, and carries risks that are not present in other flows. You should only use this flow when other more secure flows, such as managed identities, aren't viable.

Move the configuration string values into an App.config file connection string, and configure the Http client in the `GetHttpClient` method.

```csharp
public static HttpClient GetHttpClient(string connectionString, string clientId, string redirectUrl, string version = "v9.2")
{
    string url = GetParameterValueFromConnectionString(connectionString, "Url");
    string username = GetParameterValueFromConnectionString(connectionString, "Username");
    string password = GetParameterValueFromConnectionString(connectionString, "Password");
    try
    {
        HttpMessageHandler messageHandler = new OAuthMessageHandler(url, clientId, redirectUrl, username, password,
                        new HttpClientHandler());

        HttpClient httpClient = new HttpClient(messageHandler)
        {
            BaseAddress = new Uri(string.Format("{0}/api/data/{1}/", url, version)),

            Timeout = new TimeSpan(0, 2, 0)  //2 minutes
        };

        return httpClient;
    }
    catch (Exception)
    {
        throw;
    }
}
```

See the [Enhanced QuickStart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp/EnhancedQuickStart) sample for the complete code.

Even though this example uses [HttpClient](/en-us/dotnet/api/system.net.http.httpclient).[GetAsync](/en-us/dotnet/api/system.net.http.httpclient.getasync) rather than the overridden [SendAsync](/en-us/dotnet/api/system.net.http.httpclient.sendasync), the same code flow applies for any of the [HttpClient](/en-us/dotnet/api/system.net.http.httpclient) methods that send a request.

## Connect as an app

Some apps you create aren't intended to run interactively by a user. For example, you might want to make a web client application that can perform operations on Dataverse data, or a console application that performs a scheduled task of some kind.

While you could achieve these scenarios by using credentials for an ordinary user, that user account needs a paid license. Don't use this approach.

In these cases, create a special application user that is bound to a Microsoft Entra ID registered application. Next, use either a key secret configured for the app or upload a [X.509](https://www.itu.int/rec/T-REC-X.509/en) certificate. Another benefit of this approach is that it doesn't consume a paid license.

### Requirements to connect as an app

To connect as an app, you need:

- A registered app
- A Dataverse user bound to the registered app
- Connect by using either the application secret or a certificate thumbprint

#### Register your app

When registering an app, follow many of the same steps described in [Walkthrough: Register an app with Microsoft Entra ID](walkthrough-register-app-azure-active-directory), with the following exceptions:

- You don't need to grant the **Access Dynamics 365 as organization users** permission.

    This application is bound to a specific user account.
- You must configure a secret for the app registration or upload a public key certificate.

You can create or view credentials in your app registration under **Manage** &gt; **Certificates & secrets**.

To add a certificate (public key):

1. In the **Certificates** tab, select **Upload certificate**.
2. Select the file you want to upload. It must be one of the following file types: .cer, .pem, .crt.
3. Provide a description.
4. Select **Add**.

To add a client secret (application password):

1. In the **Client secrets** tab, add a description for your client secret.
2. Select an expiration time period.
3. Select **Add**.

Important

After you save the configuration changes, a secret value is displayed. Be sure to copy the secret value for use in your client application code, as you can't access that value once you leave the page.

More information: [Add credentials](/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#add-credentials)

#### Dataverse user account bound to the registered app

First, create a custom security role that defines what access and privileges this account has within the Dataverse organization. For more information, see [Create or configure a custom security role](/en-us/power-platform/admin/database-security#create-or-configure-a-custom-security-role).

After you create the custom security role, create the user account that uses it.

#### Manually create a Dataverse application user

The procedure to create an application user can be found in the Administer Power Platform article: [Create an application user](/en-us/power-platform/admin/manage-application-users#create-an-application-user).

After creating an application user, associate the application user with the custom security role you created.

#### Connect by using the application secret

If you're connecting by using a client secret and using the [Microsoft.Xrm.Tooling.Connector](/en-us/dotnet/api/microsoft.xrm.tooling.connector).[CrmServiceClient](/en-us/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient), you can use similar code as shown here:

```csharp
string SecretID = "00000000-0000-0000-0000-000000000000";
string AppID = "00001111-aaaa-2222-bbbb-3333cccc4444";
string InstanceUri = "https://yourorg.crm.dynamics.com";

string ConnectionStr = $@"AuthType=ClientSecret;
                        SkipDiscovery=true;url={InstanceUri};
                        Secret={SecretID};
                        ClientId={AppID};
                        RequireNewInstance=true";
using (ServiceClient svc = new ServiceClient(ConnectionStr))
{
    if (svc.IsReady)
    {
    //your code goes here
    }

}
```

#### Connect by using a certificate thumbprint

If you're connecting by using a certificate and using the [Microsoft.Xrm.Tooling.Connector](/en-us/dotnet/api/microsoft.xrm.tooling.connector).[CrmServiceClient](/en-us/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient), you can use similar code as shown here:

```csharp
string CertThumbPrintId = "DC6C689022C905EA5F812B51F1574ED10F256FF6";
string AppID = "00001111-aaaa-2222-bbbb-3333cccc4444";
string InstanceUri = "https://yourorg.crm.dynamics.com";

string ConnectionStr = $@"AuthType=Certificate;
                        SkipDiscovery=true;url={InstanceUri};
                        thumbprint={CertThumbPrintId};
                        ClientId={AppID};
                        RequireNewInstance=true";
using (ServiceClient svc = new ServiceClient(ConnectionStr))
{
    if (svc.IsReady)
    {
    //your code goes here
    }

}
```

### See also

[Authentication with Microsoft Dataverse web services](authentication)[Authenticating .NET Framework applications](authenticate-dot-net-framework)[Overview of the Microsoft Authentication Library](/en-us/azure/active-directory/develop/msal-overview)