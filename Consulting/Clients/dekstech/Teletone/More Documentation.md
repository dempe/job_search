---
title: More Documentation
date_created: "2026-04-22 11:55"
date_modified: "2026-04-22 14:30"
---

46xQJXA9RVTfiVZ

```
Can you update the previous documentation you made to include this?

Following up on our phone call about updating the new product documentation. As we discussed, the current version is missing a few pieces, specifically:

- Instructions for syncing MyTeletone products
- A handful of steps around the trial flow

Could you put together full documentation for how to add a new product across all 4 of our product channels? I know each has a slightly different flow:

1. Kontakt Instrument: serial sent, Native Access download, no trial
2. Beat Pack: MyTeletone download, no trial
3. Audio Effects Plug-in: serial sent, MyTeletone download, trial
4. Instrument Plug-in: serial sent, MyTeletone download (large file size), trial

Since these steps should have been covered in the original documentation, I'm treating this as finishing the original scope rather than new work. Let me know if you see it differently before you get started.
```

## 12:00 - 14:30

- Had to add `yarn` to `nix.shell`
- Now ran `yarn dev`. Frontend running locally
- 'Native Access' means it's hosted on the Native music platform. From our perspective, the user just gets a serial number.
- 'MyTeletone download' means that *we* host the bytes, we issue the serial, and the user downloads from our app.
- So Kontakt Instrument is just a serial.  
	- **Teletone doesn't generate these at all** -- NI does
	- NI provides a list of serials to Teletone
	- Teletone stores and distributes them

## Syncing Products

- In the Teletone admin panel, go to `Products` in the left column.
- In the top right corner of the `Products` page, you will see a yellow button that says, `SYNC PRODUCTS`
- Click this button (image below)

![[Pasted image 20260422130438.png]]

## Adding Products to S3

1. Login to AWS (here is a [direct link to S3](https://us-east-2.console.aws.amazon.com/s3/home?region=us-east-2))
2. If you land on the AWS homepage, type "S3" in the search bar and click on the result
3. Once in S3, click on the bucket called `teletone-assets` ![[Pasted image 20260422130719.png]]
4. Inside `teletone-assets`, there are 3 folders
	1. `instruments` -- paid requires authorization to access content in this bucket
	2. `music` -- free music samples available on <teletoneaudio.Com>, no auth
	3. `trials` -- free non-music sample downloads, also no auth
5. Let's click on `instruments`
6. Create a new folder with your desired product name by clicking on `Create Folder` in the top right: ![[Pasted image 20260422131048.png]]
7. In the page that pops up, enter your folder name, and leave the default options
8. Click the orange `Create Folder` button in the bottom right: ![[Pasted image 20260422131159.png]]
9. After you have created your folder, it should appear in the bucket. Click on the new folder you created.
10. From here you can create subfolders (e.g., for versions) following the method above.
11. After you are done creating your folders, click the orange `Upload` button in the top right: ![[Pasted image 20260422131342.png]]
12. In the page that comes up, click `Add Files` in the top right.
13. Upload the instrument that you want from your computer.
14. When you're finished, click the orange `Upload` button in the bottom right: ![[Pasted image 20260422131520.png]]

You're product will now be on S3. You can copy the URL for your uploaded object and paste it into the Teletone admin panel as described in **Step 16** above

## Additional Examples

### Kontakt Instrument

In this example, the bytes are downloaded from Native Instruments. Teletone is only responsible for distributing the serial numbers.

In **Shopify**:

1. Set `Product Type` -> `Native Access`
2. Set `Downloads Active` -> `false`
3. Set `Requires Serial Number` -> `true`

In **Teletone admin**:

1. Skip the `FILES` tab, since there is nothing to link
2. Upload serial numbers (limit 2500) as described above in **Step 17**
3. Skip the entire trial-flow section. Kontakt has no trial through Teletone
4. Customer gets an email with a serial, enters it in Native Access (NI's app)

### Beat Pack

Beat Pack products use serials under the hood. They are still required, but the user never sees them.

In **Shopify**:

1. Set `Product Type` -> `Beat Pack`
2. Set `Downloads Active` -> `true`
3. Set `Requires Serial Number` -> `true`

In **Teletone Admin**:

1. Set `FILES` tab to the CloudFront CDN URL of your download.
	1. Check the section about "Adding products to S3"
	2. Login to AWS
	3. Enter 'S3' in the search bar and click on it
	4. Click on the `teletone-assets` bucket
	5. Click on the folder that corresponds to your download
	6. Add that link to the file input and rename it to `cdn.teletoneaudio.com` as described above in **Step 16**
2. Upload serial numbers (limit 2500) as described above in **Step 17**

Customer should now be able to download the Beat Pack product.

### Audio Effects Plug-in

Audio Effect installers live at cdn.teletoneaudio.com/instruments/{product-slug}/{version}/{filename}

For example,

- `cdn.teletoneaudio.com/instruments/silverspring/1.0.1/Silver Spring PC 1…`
- `cdn.teletoneaudio.com/instruments/prismplate/1.0.3/PrismPlate_PC_Install…`

You will need to upload new Audio Effects producsts to the `instruments` folder in S3 as described in the section, "Adding Products to S3"

In **Shopify**:

1. Set `Product Type` -> `Audio Effect`
2. Set `Downloads Active` -> `true`
3. Set `Requires Serial Number` -> `true`

In **Teletone admin**:

1. In the `FILES` tab, link to the CDN URL
2. Upload serial numbers (limit 2500) as described above in **Step 17**
3. Add the trial flow
4. Customer gets an email with a serial

### Instrument Plug-in

The process for creating an Instrument Plug-In is identical to the process for creating an Audio Effects Plug-In
