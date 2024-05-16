"""
File: validEmailAddress.py
Name: Hsin-En, Tsai
Date: May 16, 2024
------------------------------------------------------------------------------
feature1:  no '@' in str
feature2:  no strings before and after '@'
feature3:  '.' in the first or last character of the string before '@'
feature4:  there is '"' and no '.' before '@'
feature5:  '"str"' before '@'
feature6:  '..' in the str
feature7:　more than one '@' in str
feature8:　strings before and after '@'
feature9:　'\' in str
feature10:　length of string before at > 64
feature11: length of string > 255
-----------------------------------------------------------------------------
"""


import numpy as np

weight_vector = np.array([
	[-1],
	[-1],
	[-1],
	[-0.85],
	[0.6],
	[-0.67],
	[-0.5],
	[0.2],
	[-0.2],
	[-1],
	[-1]
])


# DATA_FILE = 'is_valid_email_test.txt'     # This is the file name to be processed

DATA_FILE = 'emails.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	valid_emails = 0
	count = 0
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		score = weight_vector.T.dot(feature_vector)
		if (score <= 0 and count <= 12) or (score > 0 and count > 12):
			valid_emails += 1
		count += 1
	total_emails = len(maybe_email_list)
	accuracy = (valid_emails/total_emails) * 100
	print('Accuracy of this model: ' + str(accuracy) + ' %')


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	# feature_vector = []
	feature_vector = np.zeros((len(weight_vector), 1))
	for i in range(len(weight_vector)):

		# feature1:  no '@' in str
		if i == 0:
			feature_vector[i][0] = 1 if '@' not in maybe_email else 0

		text_before_at = ''.join(maybe_email.split('@')[:-1])
		text_after_at = ''.join(maybe_email.split('@')[1:])

		# feature2:  there is no strings before and after '@'
		if i == 1:
			if not feature_vector[0]:
				feature_vector[i][0] = 1 if not text_before_at or not text_after_at else 0

		# feature3:  '.' in the first or last character of the string before '@'
		if i == 2:
			if not feature_vector[0] and not feature_vector[1]:
				feature_vector[i][0] = 1 if text_before_at[0] == '.' or text_before_at[-1] == '.' else 0

		# feature4:  there is '"' and no '.' before '@'
		if i == 3:
			if not feature_vector[0] and not feature_vector[1]:
				feature_vector[i][0] = 1 if '\"' in text_before_at and '.' not in text_before_at else 0

		# feature5:  '"str"' before '@'
		if i == 4:
			if not feature_vector[0]:
				count = text_before_at.count('\"')
				feature_vector[i][0] = 1 if count > 0 and count % 2 == 0 and '\"\"' not in maybe_email else 0

		# feature6:  '..' in the str
		if i == 5:
			feature_vector[i][0] = 1 if '..' in maybe_email else 0

		# feature7:	more than one '@' in str
		if i == 6:
			if not feature_vector[0]:
				feature_vector[i][0] = 1 if maybe_email.count('@') > 1 else 0

		# feature8:	strings before and after '@'
		if i == 7:
			feature_vector[i][0] = 1 if text_before_at and text_after_at else 0

		# feature9: '\' in str
		if i == 8:
			feature_vector[i][0] = 1 if '\\' in maybe_email else 0

		# feature10: length of string before at > 64
		if i == 9:
			feature_vector[i][0] = 1 if len(text_before_at) > 64 else 0

		# feature11: length of string > 255
		if i == 10:
			feature_vector[i][0] = 1 if len(maybe_email) > 255 else 0

	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	maybe_email_list = list()
	with open(DATA_FILE, 'r') as f:
		for line in f:
			maybe_email_list.append(line.strip())
	return maybe_email_list


if __name__ == '__main__':
	main()
